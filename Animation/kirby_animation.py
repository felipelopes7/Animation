import pygame as pg
from pygame.locals import *

pg.init()
win = pg.display.set_mode((800, 600))
sprite_sheet = pg.image.load("kirby_assett.png")

leave = False
x_sprite = 0
y_sprite = 0
kirby_x = 100
kirby_y = 400
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
        jump_start_y = kirby_y  # Guarda a posição inicial do pulo

    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            kirby_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1

            # Exibe as frames enquanto ele está pulando
            if jump_count > -2 and jump_count < 0:
                frame_index = 0  # Frames de subida
            elif jump_count < -2 and jump_count > -8:
                frame_index = 1
            else:
                frame_index = 2  # Frames de queda

            frame_y = 128  # Posição y fixa para todas as frames de pulo
            win.blit(sprite_sheet, (kirby_x, kirby_y), (frame_index * 64, frame_y, 64, 64))
        else:
            jumping = False
            jump_count = 10
            frame_index = 1  # Frame de pouso
            frame_y = 280
            kirby_y = jump_start_y  # Restaura a posição inicial após o pulo

    key = pg.key.get_pressed()
    if key[K_RIGHT]:

        y_sprite = 64
        x_sprite += 1
    elif key[K_LEFT]:

        y_sprite = 192
        x_sprite += 1
        if x_sprite > 1:
            x_sprite = 1
    else:
        y_sprite = 0
        x_sprite += 1
    if x_sprite > 2:
        x_sprite = 0

    if not jumping:
        win.blit(sprite_sheet, (kirby_x, kirby_y), (x_sprite * 64, y_sprite, 64, 64))
    else:
        win.blit(sprite_sheet, (kirby_x, kirby_y), (frame_index * 64, frame_y, 64, 64))

    pg.display.flip()
    pg.time.Clock().tick(5)
    win.fill(0)