import joystick
import sys
import time
from multiprocessing.connection import Client

# Mars Rover main client module
# Sets up a joystick and sends input
# over internet to rover unit

# Sets up client to connect with the server

client = Client(('192.168.0.27', 10003))

# Initialize joystick
joystick = joystick.Joystick()
if not joystick.isInitialized:
    print("Joystick failed initialization:", joystick.initializationError)
    exit

print("Press and hold button 11 to stop.")

# Note that button 10 is labeled 11 on the joystick.
while not joystick.isButtonPressed(10):
    x, y, z = joystick.getAxes()
    data = [x,y,z]
    print("" + str(data)) #Test
    
    client.send(data)
    time.sleep(0.1) # Set to .1 seconds to send data only every 100 ms to keep from exceeding wifi capabilities

# Close socket and notify user and server of stoppage
print("STOPPED!")
x = 2
y = 2
z = 2
data = [x,y,z]
client.send(data)
client.close()