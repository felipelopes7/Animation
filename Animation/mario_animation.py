import pygame as pg
from pygame.locals import *

pg.init()
win = pg.display.set_mode((800, 600))
sprite_sheet = pg.image.load("super_mario_sheet.png")

leave = False
x_sprite = 0
y_sprite = 0
mario_x = 100
mario_y = 400
jumping = False
jump_count = 10
jump_start_y = 0

while not leave:
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            leave = True

    key = pg.key.get_pressed()
    if key[K_SPACE] and not jumping:
        jumping = True
        jump_start_y = mario_y  # Guarda a posição inicial do pulo

    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            mario_y -= ((jump_count ** 2) * 0.5 * neg)/2
            jump_count -= 1

            # Exibe as frames enquanto ele está pulando
            if jump_count > -8:
                frame_index = 0  # Frames de subida
            else:
                frame_index = 1  # Frames de queda

            frame_y = 64  # Posição y fixa para todas as frames de pulo
            win.blit(sprite_sheet, (mario_x, mario_y), (frame_index * 32, frame_y, 32, 32))
        else:
            jumping = False
            jump_count = 10
            frame_index = 5  # Frame de pouso
            frame_y = 64
            kirby_y = jump_start_y  # Restaura a posição inicial após o pulo

    key = pg.key.get_pressed()
    if key[K_RIGHT]:

        y_sprite = 32
        x_sprite += 1
        if x_sprite > 2:
            x_sprite = 1


    elif key[K_LEFT]:

        y_sprite = 0
        x_sprite += 1
        if x_sprite > 2:
            x_sprite = 0
    else:
        #if y_sprite == 64:
         #   y_sprite = 0
        #elif y_sprite == 128:
        #    y_sprite = 0
        y_sprite = 0
        x_sprite = 0
   # if x_sprite > 2:
   #     x_sprite = 0

    if not jumping:
        win.blit(sprite_sheet, (mario_x, mario_y), (x_sprite * 32, y_sprite, 32, 32))
    else:
        win.blit(sprite_sheet, (mario_x, mario_y), (frame_index * 32, frame_y, 32, 32))

    pg.display.flip()
    pg.time.Clock().tick(5)
    win.fill(0)