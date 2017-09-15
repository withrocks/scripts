# Yanking to the clipboard by default

It's possible to copy to the clipboard on every yank (without specifying the system clipboard register). First, vim needs to be compiled with clipboard support, `echo has('clipboard')` doesn't return 0.

A simple way to get that version on debian-based is to install vim-gnome (alt. vim-gtk).

Then add this to your ~/.vimrc.

```set clipboard=unnamedplus```

Some more info: https://stackoverflow.com/a/11489440/282024
