#!/bin/bash
restic -p /opt/scripts/secret -r {{ s3_repository }} backup /docker-data/nextcloud/
