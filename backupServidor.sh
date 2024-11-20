#!/bin/bash
rsync -av -e "ssh -i /home/lucia/.ssh/clave_ssh" --link-dest=lucia@34.175.158.121:/var/tmp/Backups/$(date -d 'yesterday' +'%Y-%m-%d') /home/lucia/Escritorio/seguridad/ lucia@34.175.158.121:/var/tmp/Backups/$(date +%d-%m-%Y)
