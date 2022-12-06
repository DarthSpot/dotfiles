#!/bin/bash
export SDL_VIDEODRIVER=wayland
export MOZ_ENABLE_WAYLAND=1
export GTK_THEME=gruvbox-dark-gtk
export XDG_SESSION_DESKTOP=Hyprland
export XDG_SESSION_TYPE=wayland
export XDG_CURRENT_DESKTOP=Hyprland
exec Hyprland
