import pygame
import PyParticles

pygame.display.set_caption("Tutorial 10")
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

env = PyParticles.Environment(width, height)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  env.update()
  screen.fill(env.color)

  for p in env.particles:
    pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), p.size, p.thickness)

  pygame.display.flip()