#!/usr/bin/env python3

import os

secret_location = "/opt/scripts/secret"
repo_location = "/nfs-share/backup/docker-data_{{ ansible_hostname }}"
os.system(f"restic forget -w 1 -p {secret_location} -r {repo_location}")
os.system(f"restic prune -p {secret_location} -r {repo_location}")

