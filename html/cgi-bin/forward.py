#!/usr/bin/python

import drivetrain
import cgi
import time

print ("Content-type: text/html");
print ("Status: 204 No Content\n\n");
#This is the script for forward movement via mouse

driveTrain = drivetrain.DriveTrain()
driveTrain.setTurnSpeedDivisor(2)
driveTrain.setLongitudinalSpeedDivisor(6)

#values x, y, z where y is -0.2 to indicate forward movement at 20% available speed.
driveTrain.driveHybrid(0,-1, 0)
time.sleep(2)