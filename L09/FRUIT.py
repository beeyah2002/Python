from random import randint
import pgzrun

width = 640
height = 480

apple = Actor('orange')

def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(10,600)
    apple.y = randint(10,400)
place_apple()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('You missed')

pgzrun.go()