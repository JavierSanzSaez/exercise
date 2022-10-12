import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('group', type=str, help='The group from which to copy all folders')
parser.add_argument('destination',type=str, help='The destination folder')
args = parser.parse_args()

group = args.group
destination = args.destination


def move(group:str, destination:str) -> None:
    pass

def checks(group:str)->None:
    group_shell = subprocess.run('groups', capture_output=True)
    group_list = group_shell.stdout.decode().replace("\n", "").split(" ") # The output is in bytes, so we decode it, clean it and split it

    if group not in group_list:
        raise Exception("Input group is not an existing group of the system. Please check it is correctly written")
    

if __name__ == "__main__":
    checks(group=group)
    move(group=group, destination=destination)