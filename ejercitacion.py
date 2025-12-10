from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


from robot import Robot

left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, Direction.CLOCKWISE)
#ultrasonido = UltrasonicSensor(Port.C)
color = ColorSensor(Port.E)


r2 = Robot(left_motor, right_motor,90,90)
#r2.guardar_sensor('ultra', ultrasonido)
r2.guardar_sensor('color', color)

freq = {
    Color.RED: 250,
    Color.BLUE: 1000,
    Color.WHITE: 500,
    Color.GREEN: 750,
}

 #El robot comienza en la esquina 1 mirando al norte

movimientos = {
    (Color.RED, 2 , "Norte"): [ [ ('turn',(90,)), ('straight', (800,)) ], 1, "Oeste"],
    (Color.RED, 2 , "Sur"): [ [ ('turn',(-90,)), ('straight', (800,)) ], 1, "Oeste"],
    (Color.RED, 2 , "Este"): [ [ ('turn',(180,)), ('straight', (800,)) ], 1, "Oeste"],
    (Color.RED, 2 , "Oeste"): [ [ ('straight', (800,)) ], 1, "oeste"],

}

esquina = 2
orientacion = "Norte"
while True:
    sensor = r2.sensor('color').color()
    key = (sensor, esquina, orientacion)
    historia, esquina, orientacion = movimientos.get(key)
    print(key)
    r2.beep(freq[sensor], 1000)
    r2.hacer_historia(historia)    

#Suponemos que el robot coiensa en la esquina 1 mirando al sur 
#
# 1   2               Norte           Rojo       Amarillo
#               Oeste       Este   
#                      Sur
# 3   4                               Azul       Verde

#Rojo=>ir a la esquina 1
#Verde=>ir la esquina 3
#Azul=>ir a la esquina 4
#Amarillo=>ir a la esquina 2


movimientos= {
    (Color.RED, 1 ,"Norte"): , 1, "Norte"],
    (Color.RED, 1 ,"Sur"): , 1, "Sur"],
    (Color.RED, 1 ,"Este"):, 1, "Este"],
    (Color.RED, 1 ,"Oeste"):, 1, "Oeste"],
    
    (Color.RED, 2 ,"Norte"): [ [('turn',(-90,)), ('straight', (800,))], 1, "Oeste"],
    (Color.RED, 2 ,"Sur"): [ [('turn',(90,)), ('straight', (800,))], 1, "Oeste"],
    (Color.RED, 2 ,"Este"): [ [('turn',(90,)), ('straight', (800,))], 1, "Oeste"],
    (Color.RED, 2 ,"Oeste"): [ [('turn',(90,)), ('straight', (800,))], 1, "Oeste"],
    































































































































































































































































































































































#hola:)    