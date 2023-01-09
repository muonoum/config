#!/bin/bash
[ -f $HOME/.cache/tmux/last-layout ] && 
tmux select-layout $(cat $HOME/.cache/tmux/last-layout)
