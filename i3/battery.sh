#!/bin/bash

git clone https://github.com/rjekker/i3-battery-popup.git ~/.i3-battery-popup

echo "exec --no-startup-id ~/.i3-battery-popup/i3-battery-popup" >> ~/.config/i3/config

