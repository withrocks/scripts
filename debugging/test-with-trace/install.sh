#!/bin/bash

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# TODO: copy instead of ln
cp $DIR/test-with-trace /usr/bin/test-with-trace
cp $DIR/test-with-trace.py /usr/bin/test-with-trace.py

