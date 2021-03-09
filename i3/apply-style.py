#!/usr/bin/env python
from jinja2 import Template
import sys

solarized = {
    "base03": "#002b36",
    "base02": "#073642",
    "base01": "#586e75",
    "base00": "#657b83",
    "base0": "#839496",
    "base1": "#93a1a1",
    "base2": "#eee8d5",
    "base3": "#fdf6e3",
    "yellow": "#b58900",
    "orange": "#cb4b16",
    "red": "#dc322f",
    "magenta": "#d33682",
    "violet": "#6c71c4",
    "blue": "#268bd2",
    "cyan": "#2aa198",
    "green": "#859900",
}

fname = sys.argv[1]
theme = sys.argv[2]


# SELECTION OF THEME

if theme == "dark":
    content = solarized["base0"]
    background = solarized["base03"]
    background_highlight = solarized["base02"]

    emp_content = solarized["base1"]
    secondary_content = solarized["base01"]
else:
    content = solarized["base00"]
    background = solarized["base3"]
    background_highlight = solarized["base2"]

    emp_content = solarized["base01"]
    secondary_content = solarized["base1"]

# AFTER SELECTING THEME

# Start with solarized itself, so we can directly reference the colors
styles = dict(**solarized)

with open(fname) as fs:
    templ = Template(fs.read())

styles.update({
   "background_highlight": background_highlight,
   "background": background,
   "content": content,
   "emp_content": emp_content,
   "secondary_content": secondary_content,
})

rendered = templ.render(**styles)

print(rendered)
