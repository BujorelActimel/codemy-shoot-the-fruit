import os
import pgzrun

WIDTH, HEIGHT = 600, 600

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

apple = Actor('apple')

def on_mouse_down(pos):
    pass

def draw():
    screen.fill((0, 125, 200))
    apple.draw()

pgzrun.go()
