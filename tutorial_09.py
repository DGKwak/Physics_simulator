import pygame
import random
import math

background_colour = (255, 255, 255)
width, height = 300, 200
gravity = (math.pi, 0.002)
elasticity = 0.75
mass_of_air = 0.2

def add_vectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    
    return angle, length

def collide(p1, p2):
  dx = p1.x - p2.x
  dy = p1.y - p2.y

  distance = math.hypot(dx, dy)

  if distance < p1.size + p2.size:
    angle = math.atan2(dy, dx) + 0.5 * math.pi
    total_mass = p1.mass + p2.mass

    p1.angle, p1.speed = add_vectors(p1.angle, 
                                     p1.speed * (p1.mass - p2.mass) / total_mass,
                                     angle,
                                     2 * p2.speed * p2.mass / total_mass)
    p2.angle, p2.speed = add_vectors(p2.angle,
                                     p2.speed * (p2.mass - p1.mass) / total_mass,
                                     angle + math.pi,
                                     2 * p1.speed * p1.mass / total_mass)

    p1.speed *= elasticity
    p2.speed *= elasticity
    
    overlap = 0.5 * (p1.size + p2.size - distance + 1)
    p1.x += math.sin(angle) * overlap
    p1.y -= math.cos(angle) * overlap
    p2.x -= math.sin(angle) * overlap
    p2.y += math.cos(angle) * overlap

def find_particle(particles, x, y):
  for p in particles:
    if math.hypot(p.x - x, p.y - y) <= p.size:
      return p
  
  return None

class Particle:
  def __init__(self, x, y, size, mass=1):
    self.x = x
    self.y = y
    self.size = size
    self.mass = mass
    self.colour = (0, 0, 255)
    self.thickness = 1
    self.speed = 0.01
    self.angle = math.pi / 2
    self.drag = (self.mass / (self.mass + mass_of_air)) ** self.size
    
  def display(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
    
  def move(self):
    self.x += math.sin(self.angle) * self.speed 
    self.y -= math.cos(self.angle) * self.speed
    
    self.speed *= self.drag
    
  def bounce(self):
    if self.x > width - self.size:
      self.x = 2 * (width - self.size) - self.x
      self.angle = -self.angle
      self.speed *= elasticity
      
    elif self.x < self.size:
      self.x = 2 * self.size - self.x
      self.angle = -self.angle
      self.speed *= elasticity
      
    if self.y > height - self.size: 
      self.y = 2 * (height - self.size) - self.y
      self.angle = math.pi - self.angle
      self.speed *= elasticity
      
    elif self.y < self.size:
      self.y = 2 * self.size - self.y
      self.angle = math.pi - self.angle
      self.speed *= elasticity

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')

num_of_particles = 3
particle_list = []

for _ in range(num_of_particles):
  size = random.randint(10, 20)
  density = random.randint(1, 20)
  x = random.randint(size, width - size)
  y = random.randint(size, height - size)
  
  particle = Particle(x, y, size, density * size ** 2)
  particle.speed = random.random()
  particle.angle = random.uniform(0, math.pi*2)
  particle.colour = (200 - density * 10, 200 - density * 10, 255)
  
  particle_list.append(particle)

selected_particle = None
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouseX, mouseY = pygame.mouse.get_pos()
      selected_particle = find_particle(particle_list, mouseX, mouseY)
    elif event.type == pygame.MOUSEBUTTONUP:
      selected_particle.colour = (0, 0, 255)
      selected_particle = None
  
  screen.fill(background_colour)
  
  if selected_particle:
    selected_particle.colour = (255, 0, 0)
    mouseX, mouseY = pygame.mouse.get_pos()
    dx = mouseX - selected_particle.x
    dy = mouseY - selected_particle.y
    selected_particle.angle = math.atan2(dy, dx) + 0.5 * math.pi
    selected_particle.speed = math.hypot(dx, dy) * 0.1

  for i, particle in enumerate(particle_list):
    if particle != selected_particle:
      particle.move()
      particle.bounce()
    
    for particle2 in particle_list[i+1:]:
      collide(particle, particle2)
    
    particle.display()
    
  pygame.display.flip()