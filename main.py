import random as rand
import pygame as py
import os

# Change the current working directory to the folder where your script is located
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

screen = py.display.set_mode((680, 680))

class Image():
    def __init__(self, Folder):
        self.Image = py.image.load(rf"{Folder}/{rand.randint(1,6)}.png").convert_alpha()
        self.Rect = self.Image.get_rect()
        self.Mask = py.mask.from_surface(self.Image)

screen.blit(Image("Dice1").Image, (20,20))
screen.blit(Image("Dice2").Image, (240,20))
screen.blit(Image("Dice3").Image, (460,20))
screen.blit(Image("Dice4").Image, (20,240))
screen.blit(Image("Dice5").Image, (240,240))
screen.blit(Image("Dice6").Image, (460,240))
screen.blit(Image("Dice7").Image, (20,460))
screen.blit(Image("Dice8").Image, (240,460))
screen.blit(Image("Dice9").Image, (460,460))

py.init()
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.update()
    py.time.Clock().tick(6)
py.quit()