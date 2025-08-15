import random
import math

class Particle:
  def __init__(self, x, y, size, mass=1):
    self.x = x
    self.y = y
    self.size = size
    self.mass = mass
    self.color = (0, 0, 255)
    self.thickness = 1
    self.speed = 0.01
    self.angle = math.pi / 2
    self.drag = (self.mass / (self.mass + mass_of_air)) ** self.size
    
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

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []
        
        self.color = (255, 255, 255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75
        
    def addParticles(self, n=1, **kargs):
        for i in range(n):
            size = kargs.get('size', random.randint(10, 20))
            mass = kargs.get('mass', random.randint(100, 10000))
            x = kargs.get('x', random.uniform(size, self.width - size))
            y = kargs.get('y', random.uniform(size, self.height - size))
            
            p = Particle(x, y, size, mass)
            p.speed = kargs.get('speed', random.uniform())
            p.angle = kargs.get('angle', random.uniform(0, math.pi * 2))
            p.color = kargs.get('color', (0, 0, 255))
            p.drag = (p.mass/(p.mass + self.mass_of_air)) ** p.size
            
            self.particles.append(p)