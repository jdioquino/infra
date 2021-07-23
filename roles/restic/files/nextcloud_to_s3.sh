#!/bin/bash
restic -p /opt/scripts/secret -r s3:s3.ap-southeast-1.amazonaws.com/{{ bucket }} backup /docker-data/nextcloud/
