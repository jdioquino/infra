#!/usr/bin/env python3
import os
import subprocess


def validate_mount(directory):
    try:
        check_mount = subprocess.run([f'df -h | grep -i {directory}'], shell=True, check=True, stdout=subprocess.PIPE,
                                     universal_newlines=True)
        print(f"{directory} is currently mounted")
    except subprocess.CalledProcessError:
        print(f"Trying to mount {directory}..")
        mount = os.system("mount -a && sleep 3s")
        try:
            check_mount = subprocess.run([f'df -h | grep -i {directory}'], shell=True, check=True, stdout=subprocess.PIPE,
                                         universal_newlines=True)
            print(f"{directory} is mounted now")
        except subprocess.CalledProcessError:
            print(f"Failed to mount {directory}")


name_of_directory = "/nfs-share"
validate_mount(name_of_directory)

