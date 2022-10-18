import subprocess
import argparse
import tempfile
import shutil
from datetime import datetime
import tarfile
import logging

parser = argparse.ArgumentParser()
parser.add_argument('group', type=str, help='The group from which to copy all folders')
parser.add_argument('destination',type=str, help='The destination folder')
args = parser.parse_args()

group = args.group
destination = args.destination

logging.basicConfig(format='%(asctime)s - %(levelname)s -%(message)s', filename='output.log', filemode='a', level=logging.DEBUG)

def move(group:str, destination:str) -> None:
    # First we need to locate all files from the group
    group_files = subprocess.run(f'find $HOME/exercise -group {group}', shell=True, capture_output=True)
    group_files_list = group_files.stdout.decode().split("\n")[:-1] # The last element is empty
    
    with tempfile.TemporaryDirectory() as tmpdir: # We will archive the files to a temp folder to avoid external interference
        logging.debug(f'Creating temp folder at {tmpdir}')
        tar_filename = f'{tmpdir}/{group}-{datetime.now().strftime("%d%m%Y-%H%M%S")}.tar' # in order to provide robustness and avoid collisions, the tar file has the group and the exact datetime timestamp
        with tarfile.open(tar_filename, mode='a') as tar: 
            for file in group_files_list:
                tar.add(file, arcname=file.split(r'/')[-1]) # This only works in UNIX systems (a.k.a. not Windows)
        logging.debug(f'Tar file at {tar_filename} created succesfully')
        try:
            shutil.move(tar_filename, destination)
            logging.debug('Tar file moved succesfully')
        except Exception as e:
            logging.warning(f'Error while moving the tar file, see output below \n {e}')
            raise e
    logging.info(f'Files moved successfully to folder {destination}')


def checks(group:str, destination:str)->None:
    logging.debug(f'Parameters checked: group: {group}, destination:{destination}')
    # TODO: Sanitize group to avoid injection

    group_shell = subprocess.run(f'getent group | grep -w {group}', shell=True, capture_output=True)
    group_list = group_shell.stdout.decode() # The output is in bytes, so we decode it, clean it and split it

    if group_list=='':
        logging.warning(f'Input group "{group}" is not an existing group of the system. Please check it is correctly written')
        raise Exception(f"Input group '{group}' is not an existing group of the system. Please check it is correctly written")
    
    logging.info('Checks passed: All good')

def main():
    logging.info("Preparing to copy files...")
    checks(group=group, destination=destination)
    move(group=group, destination=destination)
    logging.info("Unimover completed successfully!")