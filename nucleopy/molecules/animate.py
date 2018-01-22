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
intro = myfont.render("This is the nucleus.",
                      False, (0,0,0))
intro2 = myfont.render("The DNA has just been transcripted to", False, (0,0,0))
screen.blit(intro, (100,20))
intro3 = myfont.render("RNA and it heads to the ribosomes.", False, (0,0,0))
screen.blit(intro2, (100,60))
screen.blit(intro3, (100,100))
s = myfont.render("DNA sequence:        "+d.sequence(), False, (0,0,0))

screen.blit(s, (100,190))

r = myfont.render("Complement RNA:   " + d.toRNA().sequence(), False, (0, 0, 0))
screen.blit(r, (100,230))
pygame.display.update()
pygame.time.wait(12000) #12000
screen.fill(pygame.Color('white'))
pygame.display.update()

begin_x = 50
begin_y = 240

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
    rib = pygame.rect.Rect((550, 320, 16, 16)) # first should be 600
    v1 = pygame.rect.Rect((515, 300, 16, 16))
    v2 = pygame.rect.Rect((500, 320, 16, 16))
    v3 = pygame.rect.Rect((300, 280, 16, 16))
    v4 = pygame.rect.Rect((325, 330, 16, 16))
    v5 = pygame.rect.Rect((410, 270, 16, 16))
    v6 = pygame.rect.Rect((460, 370, 16, 16))
    v7 = pygame.rect.Rect((430, 315, 16, 16))

    m1 = myfont.render("This is the cytoplasm.",
                          False, (0, 0, 0))
    m2 = myfont.render("Guide the mRNA to the purple ribosome.", False, (0, 0, 0))
    m3 = myfont.render("Watch out for the red viruses!",False, (0,0,0))


    screen.fill(pygame.Color('white'))
    screen.blit(m1, (100, 20))
    screen.blit(m2, (100, 60))
    screen.blit(m3, (100, 100))
    pygame.draw.circle(screen, pygame.Color('pink'), (0, 250), 150)
    pygame.draw.rect(screen, pygame.Color('blue'), r)
    pygame.draw.rect(screen, pygame.Color('purple'), rib)
    pygame.draw.rect(screen, pygame.Color('red'), v1)
    pygame.draw.rect(screen, pygame.Color('red'), v2)
    pygame.draw.rect(screen, pygame.Color('red'), v3)
    pygame.draw.rect(screen, pygame.Color('red'), v4)
    pygame.draw.rect(screen, pygame.Color('red'), v5)
    pygame.draw.rect(screen, pygame.Color('red'), v6)
    pygame.draw.rect(screen, pygame.Color('red'), v7)
    pygame.display.update()

    if r.colliderect(rib):
        final = True
        break
    if r.colliderect(v1) or r.colliderect(v2) or r.colliderect(v3) or r.colliderect(v4) or \
            r.colliderect(v5) or r.colliderect(v6) or r.colliderect(v7):
        break

if not final:
    screen.fill(pygame.Color('white'))
    l = myfont.render("You Lose", False, (0,0,0))
    screen.blit(l,(100,50))
    pygame.display.update()
    pygame.time.wait(5000)

while final:
    screen.fill(pygame.Color('purple'))

    e1 = myfont.render("You made it to the ribosome!",
                          False, (0, 0, 0))
    e2 = myfont.render("The RNA is transcripted to amino acids, ", False, (0, 0, 0))
    screen.blit(e1, (100, 20))
    e3 = myfont.render("which form proteins. The proteins are ", False, (0, 0, 0))
    e4 = myfont.render("then transported to the rest of the body.", False, (0,0,0))
    screen.blit(e2, (100, 60))
    screen.blit(e3, (100, 100))
    screen.blit(e4, (100, 140))

    newrna = d.toRNA()
    s = myfont.render("RNA sequence: " + newrna.sequence(), False, pygame.Color('white'))
    screen.blit(s, (100, 230))
    r = myfont.render("Protein:             " + newrna.toProtein(), False, pygame.Color('white'))
    screen.blit(r, (100, 270))
    pygame.display.update()
