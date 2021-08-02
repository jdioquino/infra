#!/bin/bash
restic -p /opt/scripts/secret -r {{ s3_nextcloud }} backup /docker-data/nextcloud/ && wget http://hea.{{ domain_name }}/ping/{{ hc_id3 }} && rm -rf {{ hc_id3 }}
