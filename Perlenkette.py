#Diese Übung wurde mit Pygame durchgeführt

import pygame as pg

background_colour = (255,255,255)
(width, height) = (1200, 200)
color = (0,0,0)
screen = pg.display.set_mode((width, height))


pg.display.set_caption('Drawing')
screen.fill(background_colour)
pg.draw.circle(screen, color, [80, 80], 80, 1)
pg.draw.circle(screen, color, [240, 80], 80, 1)
pg.draw.circle(screen, color, [400, 80], 80, 1)
pg.draw.circle(screen, color, [560, 80], 80, 1)
pg.draw.circle(screen, color, [720, 80], 80, 1)

pg.display.update()

#Loop
running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
      pg.quit()
