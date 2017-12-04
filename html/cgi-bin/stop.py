#!/usr/bin/python
import drivetrain
import cgi

print "Content-type: text/html";
print "Status: 204 No Content\n\n";
#This is the script for stopped movement via mouse
driveTrain = drivetrain.DriveTrain()
driveTrain.setTurnSpeedDivisor(2)
driveTrain.setLongitudinalSpeedDivisor(6)

#values x, y, z where all values are 0 to end movement
driveTrain.stop()