#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# Set the speed, acceleration, and turn rate.
robot.settings(600, 201, 455, 110)

# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacle_sensor = UltrasonicSensor(Port.S2)

# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
# The axle track is the distance between the points where the wheels
# touch the ground.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

# The following loop makes the robot drive forward until it detects an
# obstacle. Then it backs up and turns around. It keeps on doing this
# until you stop the program.
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance() > 300:
        wait(10)

    # Drive backward for 300 millimeters.
    robot.straight(-305)

    # Turn around by 120 degrees
    robot.turn(901)