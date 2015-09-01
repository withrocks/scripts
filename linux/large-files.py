#!/usr/bin/env python
import subprocess
import os.path
import re
import sys

if len(sys.argv) > 1:
    minimum = int(sys.argv[1])
else:
    minimum = 1000000

print "Usage exceeding {0} bytes".format(minimum)

def execute(params):
    proc = subprocess.Popen(params, stdout=subprocess.PIPE)
    for line in iter(proc.stdout.readline, b''):
        yield line.rstrip()
 
def get_raw_data(path):
    path = os.path.expanduser(path)
    return execute(["du", path])

def get_data(path):
    for line in get_raw_data(path):
        match = re.match(r"(\d+)\s+(.*)", line)
        if match:
            yield int(match.groups()[0]), match.groups()[1]

data = get_data("~")
data = (entry for entry in data if entry[0] >= minimum)
for entry in sorted(data, reverse=True):
    print "{0} {1}".format(entry[0], entry[1])

