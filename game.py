
import time
import random
from turtle import right
import pygame
pygame.init()
white = (255,255,255)
height = 1080
width = 720



# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


snake_speed = 20
snake_positon = [600,300] # snake initial positon
snake_body = [
    [600,300],
    [590,300],
    [580,300],
    [570,300]
]

fruit_postion = [random.randrange(1, (height//10))*10
                ,random.randrange(1 , (width//10))*10  ]

fruit_spwan = True

snake_dir = 'right'
change_to = snake_dir

score = 0

def show_score(color , font , size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)



fps = pygame.time.Clock()
display_surface = pygame.display.set_mode((height,width))

pygame.display.set_caption("First game")

snake_image = pygame.image.load(r"C:\Users\india\Downloads\snake.jpg")
apple_image = pygame.image.load(r'C:\Users\india\Downloads\apple.jpg')
bg_image = pygame.image.load(r'C:\Users\india\Downloads\bg.jpg')

while True:
    display_surface.fill(white)
    display_surface.blit(bg_image,(0,0))
    event = pygame.event.wait()
    if event.type in (pygame.KEYDOWN,pygame.KEYUP):
        key_name = pygame.key.name(event.key)

        key_name = key_name.upper()

        if event.type == pygame.KEYDOWN:
            print("this key was pressed" , key_name)
        elif event.type == pygame.KEYUP:
            print("this key was released" , key_name)



    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update()

