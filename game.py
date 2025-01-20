import os
import random
import pgzrun

WIDTH, HEIGHT = 800, 600

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

def getHighscore(file):
    with open(file, "r") as f:
        line = f.readline()
        return int(line)
    
def saveHighscore(file, score):
    with open(file, "w") as f:
        f.write(str(score))

fructe = [Actor('apple'), Actor('orange'), Actor('pineapple')]
fruct_curent = random.choice(fructe)
score = 0
highscore = getHighscore("highscore.txt")
missed = False

def move(fruit):
    fruit.x = random.randint(50, 750)
    fruit.y = random.randint(50, 550)

def on_mouse_down(pos):
    global fruct_curent, score, missed
    if missed:
        return

    random_sound = random.choice([sounds.splatter1, sounds.splatter2, sounds.splatter3, sounds.splatter4])
    random_sound.play()
    if fruct_curent.collidepoint(pos):
        print("ai nimerit")
        score += 1
        fruct_curent = random.choice(fructe)
        move(fruct_curent)
    else:
        missed = True

def draw():
    global highscore
    screen.fill((0, 125, 200))
    if missed:
        screen.draw.text("Ai pierdut", (350, 300))
        screen.draw.text(f"Ai avut scorul {score}", (335, 330))
        if score > highscore:
            screen.draw.text("New Highscore!", (350, 270))
            highscore = score
            saveHighscore("highscore.txt", highscore)
    else:
        screen.draw.text(f"Score: {score}", (675, 20))
        fruct_curent.draw()

pgzrun.go()
