#!/bin/bash

dir="~/screenshots"
mkdir -p $dir
scrot 'screenshot_%Y%m%d_%H%M%S.png' -e 'mv $f ${dir} && xclip -selection clipboard -t image/png -i ${dir}`ls -1 -t ${dir} | head -1`' # All screens
