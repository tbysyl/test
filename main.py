import pygame as pg
import random
import math

rad = 50

class Boid:
    def __init__(self,x,y,r,s):
        self.x = x
        self.y = y
        self.r = r
        self.s = s
        self.a = random.uniform(0, 2) * math.pi

    def move(self):
        self.x += self.s * math.cos(self.a)
        self.y += self.s * math.sin(self.a)

        if self.x - self.r < 0 or self.x + self.r > width:
            self.a = math.pi - self.a
        if self.y - self.r < 0 or self.y + self.r > height:
            self.a = -self.a

    def draw(self,surface):
        pg.draw.circle(surface,(0,0,255),(int(self.x),int(self.y)),self.r)

pg.init()

width,height = 800,600
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Boids")

boids = []
boids.append(Boid(random.randint(0,width-rad),random.randint(0,height-rad),rad,random.uniform(0,15)))

clock = pg.time.Clock()
last_spawn_time = pg.time.get_ticks()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()  

    screen.fill((0,0,0))

    current_time = pg.time.get_ticks()
    if current_time - last_spawn_time >= 100:  
        new_boid = Boid(random.randint(0,width-(rad+1)),random.randint(0,height-(rad+1)),rad,random.uniform(0,15))
        boids.append(new_boid)
        last_spawn_time = current_time  

    for boid in boids:
        boid.move()
        boid.draw(screen)

    pg.display.flip()
    clock.tick(60) 

pg.quit()
