import joystick
import socket
import sys
import time
import pickle

# Mars Rover main client module
# Sets up a joystick and sends input
# over internet to rover unit

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.0.27', 10003)
sock.connect(server_address)

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
    dataSend = pickle.dumps(data)

    sock.sendall(dataSend)
    time.sleep(0.1) # Set to .1 seconds to send data only every 100 ms to keep from exceeding wifi capabilities

# Close socket and notify user and server of stoppage
print("STOPPED!")
x = 2
y = 2
z = 2
data = [x,y,z]
dataSend = pickle.dumps(data)
sock.sendall(dataSend)
sock.close()