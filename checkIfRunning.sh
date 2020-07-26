#!/bin/sh
#thanks Chris Elgee (2018) for the original code from soundboard project 

if pgrep -f "python3 plantPal.py"; then
    pid=$(pidof python3 plantPal.py)
    echo "pid of plantPal:" $pid
    echo "it is already running"
    exit
else
    echo "starting sound board!"
    cd /home/pi/PlantPal/
    python3 plantPal.py &
    pid=$(pidof python3 plantPal.py)
    echo "pid of plantPal:" $pid
fi

exit 0 
