# Pace calculator
Simple pace calculator for dev runners

## About
Pace, also called rhythm or tempo, is the rate of activity or movement, such as in running or the flow of events in an entertainment piece. This script helps you get your current pace (min/km) and average speed (km/h) on the current running, given the distance (km) and your time (00h 00m 00s).

## Starting
Clone or download the script on this repository and run it on terminal.

First parameter is always your distance (km)
Second parameter is your time. You can send only a string with the value(00h00m00s) or split it in more two parameters (00h 00m 00s)

Ex.: Run with 10km on 55 minutes and 36 seconds
```bash
$ pace.py 10 55m36s
```
Outputs
```bash
>>> ================================
>>> Distance:       10km
>>> --------------------------------
>>> Time:           0h 55' 36"
>>> --------------------------------
>>> PACE:           5.33 min/km
>>> --------------------------------
>>> AVG Speed:      10.79 km/h
>>> ================================
```
