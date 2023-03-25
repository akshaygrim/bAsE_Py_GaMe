import pygame
import time
import random


pygame.init()
height=1200
width=659
screen = pygame.display.set_mode((height,width))  
pygame.display.set_caption("1st game")
image= pygame.image.load(r"C:\Users\india\Downloads\game.jpg")
color= (255,255,255)
fps = pygame.time.Clock()
snake_speed=20

while True:
    screen.fill(color)
    screen.blit(image, (0,0))
    event = pygame.event.wait() 
    
    if event.type in(pygame.KEYDOWN , pygame.KEYUP):
        key_name= pygame.key.name(event.key)
        
        key_name = key_name.upper()
        if event.type== pygame.KEYDOWN:
            print(u"{} " 'this key was pressed'.format(key_name))
            storekeyname = key_name
            print(storekeyname)
        elif event.type==pygame.KEYUP:
            print(u"{} " 'this key was released'.format(key_name))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()