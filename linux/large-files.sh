#!/bin/bash

search_path=$1
if [ "$search_path" == "" ]; then
  search_path=~
fi

echo "Files in $search_path using at least 1G"
du -h $search_path | grep '^\S*[GT]'
