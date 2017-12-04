import drivetrain
import time
import socket
import sys
import pickle

# A prototype of the Mars Rover main module
# which contains an infinite loop to process
# joystick input.

driveTrain = drivetrain.DriveTrain()
driveTrain.setTurnSpeedDivisor(2.5)
driveTrain.setLongitudinalSpeedDivisor(2)

# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port

server_address = ('192.168.0.27', 10003)
sock.bind(server_address)

# Listen for incoming connections

sock.listen(1)

while True:

    # Wait for a connection

    (connection, client_address) = sock.accept()

    # Receive data as a read only file

    while True:
        data = connection.makefile("r")

        if data:
            data = pickle.load(data)
            print('Data: ' + str(data))
            x = float(data[0])
            y = float(data[1])
            z = float(data[2])

                        # to create a dead zone for joystick preventing unneccessary input

            if abs(x) < 0.3:
                x = 0
            if abs(y) < 0.3:
                y = 0
            if abs(z) < 0.3:
                z = 0

            if x == 2 and y == 2 and z == 2:
                break

            # Send data to drivetrain every .1sec

            driveTrain.driveHybrid(x, y, z)
            time.sleep(0.1)
    break

driveTrain.stop()
connection.close()


			