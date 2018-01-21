import os
import pygame
from nucleopy.molecules.dna import DNA
import time

d = DNA('accgcctaggac')
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Helvetica", 35)
size = 720, 480
screen = pygame.display.set_mode(size)

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64,200,45,15))

    def handle_keys(self):
        while True:
            pygame.display.update()
            key = pygame.key.get_pressed()
            dist = 1
            if key[pygame.K_LEFT]:
               self.rect.move_ip(-1, 0)
            if key[pygame.K_RIGHT]:
               self.rect.move_ip(1, 0)
            if key[pygame.K_UP]:
               self.rect.move_ip(0, -1)
            if key[pygame.K_DOWN]:
               self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)

class Ribosome(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64, 54, 16, 16))

    def handle_keys(self):
        while True:
            pygame.display.update()
            key = pygame.key.get_pressed()
            dist = 1
            if key[pygame.K_LEFT]:
               self.rect.move_ip(-1, 0)
            if key[pygame.K_RIGHT]:
               self.rect.move_ip(1, 0)
            if key[pygame.K_UP]:
               self.rect.move_ip(0, -1)
            if key[pygame.K_DOWN]:
               self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)


now = time.time()
future = now + 5
b = True

screen.fill(pygame.Color('pink'))
s = myfont.render("DNA sequence:        "+d.sequence(), False, (0,0,0))

screen.blit(s, (100,190))

r = myfont.render("Complement RNA:   " + d.toRNA().sequence(), False, (0, 0, 0))
screen.blit(r, (100,230))
pygame.display.update()
pygame.time.wait(2000)
screen.fill(pygame.Color('white'))
pygame.display.update()

begin_x = 50
begin_y = 200

# rect = pygame.rect.Rect((64,200,begin_x,begin_y))
# rib = pygame.rect.Rect((200, 250, 16, 16))
# pygame.draw.circle(screen, pygame.Color('pink'), (0,250), 150)
# pygame.draw.rect(screen, pygame.Color('blue'), rect)

# player = Player()
# rib = Ribosome()
# rib.draw(screen)
# player.draw(screen)
# player.handle_keys()
# pygame.display.update()
# if pygame.event.get()[0].key == pygame.K_RIGHT:
#     begin_x += 10
# pygame.time.wait(10000)

final = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                begin_x += 10
            if event.key == pygame.K_LEFT:
                begin_x -= 10
            if event.key == pygame.K_UP:
                begin_y -= 10
            if event.key == pygame.K_DOWN:
                begin_y += 10

    r = pygame.rect.Rect((begin_x, begin_y, 70, 15))
    rib = pygame.rect.Rect((50, 40, 16, 16)) # first should be 600

    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('pink'), (0, 250), 150)
    pygame.draw.rect(screen, pygame.Color('blue'), r)
    pygame.draw.rect(screen, pygame.Color('purple'), rib)
    pygame.display.update()

    if r.colliderect(rib):
        final = True
        break


while final and True:
    screen.fill(pygame.Color('purple'))
    newrna = d.toRNA()
    s = myfont.render("RNA sequence: " + newrna.sequence(), False, pygame.Color('white'))
    screen.blit(s, (100, 190))
    r = myfont.render("Protein:             " + newrna.toProtein(), False, pygame.Color('white'))
    screen.blit(r, (100, 230))
    pygame.display.update()
