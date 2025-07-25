import pygame
import random
import math

background_colour = (255, 255, 255)
width, height = 300, 200

class Particle:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
    self.colour = (0, 0, 255)
    self.thickness = 1
    self.speed = 0.01
    self.angle = math.pi / 2
    
  def display(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
    
  def move(self):
    self.x += math.sin(self.angle) * self.speed 
    self.y -= math.cos(self.angle) * self.speed

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

num_of_particles = 10
particle_list = []

for _ in range(num_of_particles):
  size = random.randint(10, 20)
  x = random.randint(size, width - size)
  y = random.randint(size, height - size)
  
  particle = (Particle(x, y, size))
  particle.speed = random.random()
  particle.angle = random.uniform(0, math.pi*2)
  
  particle_list.append(particle)

for particle in particle_list:
  particle.move()
  particle.display()

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False