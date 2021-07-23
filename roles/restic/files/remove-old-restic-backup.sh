#!/bin/bash
restic forget -w 1 -p /opt/scripts/secret -r /nfs-share/backup/docker-data_node-2
restic prune -p /opt/scripts/secret -r /nfs-share/backup/docker-data_node-2
