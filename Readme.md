# RPI Fan Controller scripts
This is a backup of a couple of scripts that i used for controlling the Fan speed on my RPI. The fan speed will depend from the CPU temperature of the RPI. I adapted from a base code of Zigurana repo. 
NOTE: DO NOT CONNECT THE FAN DIRECTLY ON THE RPI! Use a Transistor Instead. Read the FAQ for more info. 


### What it is

There are two scripts:
- The python script that is used to control the fan.. when executed it should stay alive forever. It will check the CPU temperature every 6 seconds and adjust the Fan Speed accordingly using GPIO PWM. 
- The second scripts is a bash script that just make sure that the first script is always running... It will check that the process exist..if it does, it will just exit, otherwise it will launch the python code, similar to a systemctl service.

### How to use it.
	1- Make sure you have the wiringpi Library installed (pip install wiringpi)
	2- Connect your Fan to GND and #GPIO18 (physical pin 12) on rpi3
	3- Save the fan scrip folder somewhere on your rpi EG: /home/pi/fanController/ (if you change this path, fix it in the runfan.sh file)
	4- Make the scripts executable (chmod +x )
	5- Add an entry in cron that run the runfan.sh every min or so.  * * * * * /bin/bash /home/pi/fanController/runfan.sh
	6- Wait a min and now it should work...check with ps -aux if the python process exist.  


### FAQ
General:
-  Q.The fan does not spin.. why?  
- - A. Check that the python process is running. If is not than probably does not have the correct permissions. Alternatively, try to launch the python script manually and look at the log. If the process is ok, then check your fan wiring, and make sure that is connected to the right pins. 
- Q.Can I connect the FAN direclty on the RPI Pins?
- - A. No. From RPI GPIO you can draw maximum of 16mA per pin with the total current from all pins not exceeding 50mA! Your Fan Is probably exceeding that value, burning your pinout controlller. So Use a Transistor to pilot the Fan instead, and then use the RPI PIN to pilot the base of that transistor. There are many guide on how to do that online!

##### GLORY to the Great Evron Empire
