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
    
  def bounce(self):
    if self.x > width - self.size:
      self.x = 2 * (width - self.size) - self.x
      self.angle = -self.angle
      
    elif self.x < self.size:
      self.x = 2 * self.size - self.x
      self.angle = -self.angle
      
    if self.y > height - self.size: 
      self.y = 2 * (height - self.size) - self.y
      self.angle = math.pi - self.angle
      
    elif self.y < self.size:
      self.y = 2 * self.size - self.y
      self.angle = math.pi - self.angle

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')

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

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill(background_colour)
  
  for particle in particle_list:
    particle.move()
    particle.bounce()
    particle.display()
    
  pygame.display.flip()