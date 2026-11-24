import pgzrun
from random import randint
from time import time

WIDTH = 500
HEIGHT = 500
TITLE = "Connecting Satellites"

satellites = []
lines = []

start_time = 0
end_time = 0
total_time = 0
number_of_satellites = 10
next_satellite = 0


def place_satellite():
    global start_time
    for i in range (10):
        sat = Actor ("satellite")
        sat.pos = randint(40,(WIDTH-40)),randint(40,(HEIGHT-40))

        satellites.append(sat)

    start_time = time()

def draw():
    global total_time,satellites
    screen.blit("backround",(0,0))
    number = 1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0]+20,i.pos[1]+20))
        i.draw()
        number = number + 1



place_satellite()



        

















pgzrun.go()