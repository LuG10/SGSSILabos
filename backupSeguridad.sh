#!/bin/bash
rsync -av --link-dest=/var/tmp/Backups/$(date -d 'yesterday' +'%Y-%m-%d') /home/lucia/Escritorio/Seguridad/ /var/tmp/Backups/$(date +%d-%m-%Y)
