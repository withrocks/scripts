#!/bin/bash

# Generates a new key and then echos the public key
keyname=""
comment=$USER@$(hostname)
echo "Generating key for $comment"

while [ "$keyname" == "" ]
do
    echo -n "Keyname: "
    read keyname
done

ssh-keygen -t rsa -C "$comment" -b 4096 -f ~/.ssh/$keyname

cat ~/.ssh/$keyname.pub
