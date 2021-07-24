#!/bin/bash
restic -p /opt/scripts/secret -r {{ s3_bitwarden }} backup /docker-data/bitwarden/
