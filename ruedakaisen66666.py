from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from robot1 import Robot
from robot1 import Robot

left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
r = Robot(left_motor, right_motor, 85, 162)

r.straight(920)
                 
#53,5 cm

color=ColorSensor(Port.C)

r.guardar_sensor("color",color)

print(r.sensor("color"))


while True:
    c=r.sensor("color").color()
    print(c)

    if c==Color.GREEN:
        r.turn(-90)

        r.straight(920)
 
 