#!/bin/bash

function usage {
  echo "Usage: socks.sh <user>@<server>"
  exit 1
}

conn=$1

if [ -z $conn ]; then
  usage
fi

echo "Killing old instances..."
kill -9 $(lsof -i:8123 -t) 2> /dev/null

echo "SSHing using SOCKS protocol on port 8123..."
caffeinate -s ssh -D 8123 -f -C -q -N $conn

echo "Starting firefox using the socks profile, configured to use a socks proxy"
echo " - First run: Open Preferences/Network Proxy and set SOCKS Host = (localhost, 8123)"
/Applications/Firefox.app/Contents/MacOS/firefox-bin -P socks &
