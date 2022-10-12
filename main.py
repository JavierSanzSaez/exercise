import subprocess
import argparse
import tempfile
import shutil
import os
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument('group', type=str, help='The group from which to copy all folders')
parser.add_argument('destination',type=str, help='The destination folder')
args = parser.parse_args()

group = args.group
destination = args.destination


def move(group:str, destination:str) -> None:
    # First we need to locate all files from the group
    group_files = subprocess.run(f'find $HOME/exercise -group {group}', shell=True, capture_output=True)
    group_files_list = group_files.stdout.decode().split("\n")[:-1] # The last element is empty
    print(group_files_list)
    
    with tempfile.TemporaryDirectory() as tmpdir: # We will archive the files to a temp folder to avoid external interference
        with tarfile.open(f'{tmpdir}/{group}.tar', mode='a') as tar:
            for file in group_files_list:
                tar.add(file, arcname=file.split(r'/')[-1]) # This only works in UNIX systems (a.k.a. not Windows)
        shutil.move(f"{tmpdir}/{group}.tar", destination)


def checks(group:str)->None:
    # TODO: Sanitize group to avoid injection

    group_shell = subprocess.run(f'getent group | grep -w {group}', shell=True, capture_output=True)
    group_list = group_shell.stdout.decode() # The output is in bytes, so we decode it, clean it and split it

    if group_list=='':
        raise Exception("Input group is not an existing group of the system. Please check it is correctly written")

if __name__ == "__main__":
    checks(group=group)
    move(group=group, destination=destination)