#!/bin/env bash

# Options for powermenu
lock=""
logout=""
shutdown=""
reboot=""
sleep=""

# Get answer from user via rofi
selected_option=$(echo "$lock
$logout
$sleep
$reboot
$shutdown" | rofi -dmenu\
                  -i\
                  -p "Power"\
		  -theme "~/.config/rofi/scripts/powertheme.rasi"\
	  )
# Do something based on selected option
if [ "$selected_option" == "$lock" ]
then
    loginctl lock-session
elif [ "$selected_option" == "$logout" ]
then
    loginctl terminate-user "spot"
elif [ "$selected_option" == "$shutdown" ]
then
    systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
    systemctl reboot
elif [ "$selected_option" == "$sleep" ]
then
    amixer set Master mute
    systemctl suspend
else
    echo "No match"
fi
