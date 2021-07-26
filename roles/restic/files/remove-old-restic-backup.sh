#!/bin/bash
restic forget -w 1 -p /opt/scripts/secret -r /nfs-share/backup/docker-data_{{ ansible_hostname }}
restic prune -p /opt/scripts/secret -r /nfs-share/backup/docker-data_{{ ansible_hostname }}
