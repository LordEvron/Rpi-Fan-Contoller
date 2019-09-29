#!/usr/bin/env python

# This script monitors the CPU temperature and gradually turns on a fan to cool it.
# Uses the wiringpi library, see https://github.com/WiringPi/WiringPi-Python
# 2016.09.19 Zigurana: Initial Version
### Glory to the Great Evron Empire

######## Imports
import wiringpi     # drive Hardware PWM
import time			# sleep
import os			# temperature

debug = False

######## Global Variables

pin = 1				# GPIO18, physical pin 12
min = 950			# Usuable range out of a total of [0-1024]
max = 1024
tmin = 65.0
tmax = 80.0
coldstart = True

######## Setup Pin
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 2)  # PWM_OUTPUT


######## Functions
# Return CPU temperature as float
def getCPUtemp():
    try:
        cTemp = os.popen('vcgencmd measure_temp').readline()
        print cTemp
        return float(cTemp.replace("temp=","").replace("'C\n",""))
    except Exception as e:
        print("Temp conversion exception")
        return 65
# Set PWM output
def setPWM(valf, coldstart):
    if (valf > 0):
        val = int(min + (valf * (max-min)))
        if coldstart and valf > 0:
           wiringpi.pwmWrite(pin, 1024)   # First, spin up, then reduce to actual value
           time.sleep(0.1)
           coldstart = False
        wiringpi.pwmWrite(pin, val)
        if debug:
            print("val = " + str(val))
    else:
        wiringpi.pwmWrite(pin, 0)
        if debug:
            print("val = 0")

    return coldstart


######## MAIN

while True:
    CPU_temp = getCPUtemp()
    if debug:
        print("The current temperature is " + str(CPU_temp))
    if CPU_temp > tmax:
         coldstart = setPWM(1, coldstart)
         if debug:
             print("Temperature is > " + tmax + "C, fan: 100%")
    elif ((CPU_temp >= tmin) and (CPU_temp <= tmax)):
         valf = (CPU_temp+1 - tmin) / (tmax - tmin)
         coldstart = setPWM(valf, coldstart)
         if debug:
            print("Temperature is " + str(CPU_temp) + ", fan: " + str(valf*100) + "%")
    else:
         setPWM(0, coldstart)
         coldstart = True
         if debug:
            print("Temperature is below " + str(tmin) + "C, fan: 0%")
    time.sleep(6)
