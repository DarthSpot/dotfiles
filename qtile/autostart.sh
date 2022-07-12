#!/usr/bin/env bash
set -euo pipefail

feh --bg-scale /home/spot/Bilder/anime-art-fairy-tail-levy.jpg &
picom & disown

eww daemon & disown
blueberry-tray & disown
greenclip daemon & disown
mkfifo /tmp/vol && echo "$(pulsemixer --get-volume | awk '{print $1}')" > /tmp/vol & disown
mkfifo /tmp/vol-icon && ~/.config/qtile/eww_vol_icon.sh & disown
#default_startup.sh &
