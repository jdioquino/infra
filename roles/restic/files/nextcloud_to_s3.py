#!/usr/bin/env python3
import os

secret_location = "/opt/scripts/secret"
repo_location = "{{ s3_nextcloud }}"
target_backup = "/docker-data/nextcloud/"
os.system(f"restic -p {secret_location} -r {repo_location} backup {target_backup}")

