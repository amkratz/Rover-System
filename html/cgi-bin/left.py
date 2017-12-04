#!/usr/bin/python

import drivetrain
import cgi
import time

print "Content-type: text/html";
print "Status: 204 No Content\n\n";
#This is the script for left turns via mouse
driveTrain = drivetrain.DriveTrain()
driveTrain.setTurnSpeedDivisor(2)
driveTrain.setLongitudinalSpeedDivisor(6)

#values x, y, z where z is -0.5 to indicate a left turn at 50% available speed.
driveTrain.driveHybrid(0, 0, -1)
time.sleep(0.5)