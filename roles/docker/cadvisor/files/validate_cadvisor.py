#!/usr/bin/env python3
import os


def validate_container(container, directory):
    check_container = os.system(f'docker container ls | grep -i {container} &> /dev/null')
    if check_container != 0:
        os.chdir(f"/docker-data/{directory}")
        start_container = os.system('/usr/local/bin/docker-compose up -d && sleep 5s')

        if start_container != 0:
            print(f'Failed to start {container}')
        else:
            print(f'{container} is started successfully')
    else:
        print(f'{container} is currently running')
            

container = "cadvisor"
server_name = os.uname()[1]
container_name = f"{container}_{server_name}"
validate_container(container_name, container)

