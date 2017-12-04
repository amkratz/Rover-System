# MarsRoverPrototype
This repository contains prototype code for the Mars Rover.

# Overview
This rover is designed to be used over the internet using either a
joystick or mouse/web interface for control

# File Structure

### Apache Web Server
The web server is set up using Apache2, and thus it has it's own 
filesystem and documentation. The main config files that were altered 
for use with the rover are /etc/apache2/apache2.conf, 
/etc/apache2/ports.conf,
and /etc/apache2/sites-available/000default.conf.

### Web Browser Interface
The files for the website all reside within /etc/www/
  www 		- index.html
			- image files
			- buttonFunction.js
			- README.md
  
  cgi-bin	- Python scripts for motion via mouse click
			- Drivetrain.py
			- mainServer.py (kept here purely for access to drivetrain)
### Camera
The camera is controlled by Motion, which is a video streaming package,
located in /etc/motion. Camera configuration is all done using the
motion.conf file. Main settings changed were saturation set to 1 for BW
effect, and the framerate which is currently set to 24 for standard
testing.

### Client Side
The only files needed client side are joystick.py, mainClient.py, and
of course Python 3.6 and Pygame installed on the machine.

#General Use
To use the rover, you must have the rover booted and the web server
running. Run mainServer.py. Then on the client machine, with the
joystick plugged in, run mainClient.py. The robot will now be able to 
move via joystick. To see the camera feed and mouse control, you must go
to the rover website (currently set to local ip 192.168.1.182:8090) 
via web browser. The rover will now also be able to be controlled by
mouse, although using both controls at once is not currently recommended.

