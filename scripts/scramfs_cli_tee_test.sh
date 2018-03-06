#!/bin/bash

clear

echo "Create a dummy plain text file"
echo
echo "==============================================================="

scramfs alias create -e safe_dest -t onedrive -p ScramAlias.scramfs
scramfs alias create -e new_dest -t googledrive -p ScramAlias.scramfs
