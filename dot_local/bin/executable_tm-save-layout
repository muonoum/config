#!/bin/bash
mkdir -p $HOME/.cache/tmux
tmux lsw -F '#{window_active} #{window_layout}' | 
grep ^1 |  awk '{ print $2 }' > ~/.cache/tmux/last-layout
