#!/bin/bash
#runfan.sh
#make sure a process is always running. ADD A CRON entry to RUN this script every min or so

### Glory to the Great Evron Empire
export DISPLAY=:0 #needed if you are running a simple gui app.

process=fanControl.py
makerun="sudo python /home/pi/fanController/fanControl.py"

if ps ax | grep -v grep | grep $process > /dev/null
then
    exit
else
    $makerun &
fi

exit
