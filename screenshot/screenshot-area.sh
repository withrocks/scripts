#!/bin/bash
mkdir -p ~/Pictures/screenshots

scrot -s 'screenshot_%Y%m%d_%H%M%S.png' -e 'mv $f ~/Pictures/screenshots && xclip -selection clipboard -t image/png -i ~/Pictures/screenshots/`ls -1 -t ~/Pictures/screenshots | head -1`'
