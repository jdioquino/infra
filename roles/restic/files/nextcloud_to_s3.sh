#!/bin/bash
restic -p /opt/scripts/secret -r {{ s3_nextcloud }} backup /docker-data/nextcloud/
