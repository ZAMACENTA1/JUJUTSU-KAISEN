from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Robot:
    def __init__(self, left_motor, right_motor,wheel_diameter, axle_track):
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.hub = PrimeHub()
        self.drive_base.use_gyro(True)

    #Movimiento
    def straight(self, distance):
        self.drive_base.straight(distance)
        
    def turn(self, angle):
        self.drive_base.turn(angle)

    #Sonido
    def beep(self, freq, duration):
        self.hub.speaker.beep(freq, duration)

    def play_notes(self, notes):
        self.hub.speaker.play_notes(notes)

    #Luces
    def light_off(self):
        self.hub.light.off()

    def light_blink(self, color, durations):
        self.hub.light.blink(color, durations)

    def light_animate(self, colors, interval):
        self.hub.light.animate(colors, interval)

self.historia=[]
self.sensores=dict()

def guardar_sensor(self,nombre,sensor):
    self.sensores[nombre]=sensor

def sensor(self,nombre)
    return self.sensores.get(nombre)



color=ColorSensor(E)


r=Robot(...)
r.guardar_sensor("color",color)

print(r.sensor("color"))


while True:
c=r.sensor("color").color()
print(c)

if c==Color.RED
r.beep(800,1000) 

elif c==Color.BLUE
rself.historia=[]
self.sensores=dict()

def guardar_sensor(self,nombre,sensor):
…
elif c==Color.BROWN
r.beep(3000,1000)

elif c==Color.CYAN
r.beep(3100,1000)

.beep(1000,1000)

elif c==Color.WHITE
r.beep(1200,1000)

elif c==Color.GREEN
r.beep(1400,1000)

elif c==Color.YELLOW
r.beep(1600,1000)

elif c==Color.GRAY
r.beep(1800,1000)

elif c==Color.MAGENTA
r.beep(2000,1000)

elif c==Color.VIOLET
r.beep(2200,1000)

elif c==Color.ORANGE
r.beep(2400,1000)

elif c==Color.NONE
r.beep(2600,1000)

elif c==Color.BLACK
r.beep(2800,1000)

elif c==Color.BROWN
r.beep(3000,1000)

elif c==Color.CYAN
r.beep(3100,1000)
if c==Color.RED
r.beep(800,1000) 

elif c==Color.BLUE
r.beep(1000,1000)

elif c==Color.WHITE
r.beep(1200,1000)

elif c==Color.GREEN
r.beep(1400,1000)

elif c==Color.YELLOW
r.beep(1600,1000)

elif c==Color.GRAY
r.beep(1800,1000)

elif c==Color.MAGENTA
r.beep(2000,1000)

elif c==Color.VIOLET
r.beep(2200,1000)

elif c==Color.ORANGE
r.beep(2400,1000)

elif c==Color.NONE
r.beep(2600,1000)

elif c==Color.BLACK
r.beep(2800,1000)

elif c==Color.BROWN
r.beep(3000,1000)

elif c==Color.CYAN
r.beep(3100,1000)

