#!/bin/bash
export SDL_VIDEODRIVER=wayland
export MOZ_ENABLE_WAYLAND=1
export GTK_THEME=gruvbox-dark-gtk
export XDG_SESSION_DESKTOP=Hyprland
export XDG_SESSION_TYPE=wayland
export XDG_CURRENT_DESKTOP=Hyprland
export QT_QPA_PLATFORMTHEME=qt5ct
export QT_QPA_PLATFORM="wayland;xcb"
export GTK_USE_PORTAL=0
exec Hyprland
