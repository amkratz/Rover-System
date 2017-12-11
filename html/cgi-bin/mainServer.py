import drivetrain
import time
import sys
from multiprocessing.connection import Listener

# A prototype of the Mars Rover main module
# which contains an infinite loop to process
# joystick input.

driveTrain = drivetrain.DriveTrain()
driveTrain.setTurnSpeedDivisor(2)
driveTrain.setLongitudinalSpeedDivisor(2)

# Sets up the server listener to await client connection

IP_ADDRESS = 'localhost'
PORT = 10003

serverSocket = Listener((IP_ADDRESS, PORT))


while True:

    # Wait for a connection

    connection = serverSock.accept()

    # Receive data in 1024 byte chunks

    while True:
        data = connection.recv()

        if data:
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


            