#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, time

pygame.init()

screen = pygame.display.set_mode((800, 600))

black = (0, 0, 0)

pygame.display.set_icon(pygame.image.load('images/ico2.ico'))
pygame.display.set_caption("G_Game_P1 (Beta)")

bg1 = pygame.image.load('images/int/im1.jpg')
screen.blit(bg1, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg2 = pygame.image.load('images/int/im2.jpg')
screen.blit(bg2, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg3 = pygame.image.load('images/int/im3.jpg')
screen.blit(bg3, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg4 = pygame.image.load('images/int/im4.jpg')
screen.blit(bg4, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg5 = pygame.image.load('images/int/im5.jpg')
screen.blit(bg5, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg6 = pygame.image.load('images/int/im6.jpg')
screen.blit(bg6, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg7 = pygame.image.load('images/int/im7.jpg')
screen.blit(bg7, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg8 = pygame.image.load('images/int/im8.jpg')
screen.blit(bg8, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg9 = pygame.image.load('images/int/im9.jpg')
screen.blit(bg9, (0, 0))
pygame.display.update()

time.sleep(0.5)

bg10 = pygame.image.load('images/im1.png')
screen.blit(bg10, (0, 0))
pygame.display.update()

background_image = pygame.image.load('images/im1.png')


font1 = pygame.font.Font(None, 45)
text1 = font1.render(u"Данная игра является любительской сборкой.", True, black)

font2 = pygame.font.Font(None, 45)
text2 = font2.render(u"Это моя первая полная игра.", True, black)

font3 = pygame.font.Font(None, 45)
text3 = font3.render(u"Сильно не судите.", True, black)

font4 = pygame.font.Font(None, 45)
text4 = font4.render(u"Мне лень выравнивать текст.", True, black)

font5 = pygame.font.Font(None, 45)
text5 = font5.render(u"Приятной Игры.", True, black)

font6 = pygame.font.Font(None, 45)
text6 = font6.render(u"(Нажмите любую клавишу)", True, black)

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key != pygame.K_ESCAPE:
                import menu

    screen.blit(background_image, (0, 0))
    clock.tick(20)
    screen.blit(text1, [40, 50])
    screen.blit(text2, [65, 100])
    screen.blit(text3, [220, 150])
    screen.blit(text4, [120, 200])
    screen.blit(text5, [280, 250])
    screen.blit(text6, [200, 540])
    pygame.display.update()

pygame.quit()
exit()
