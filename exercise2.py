#!/usr/bin/env python
'''

For this exercise, draw a random number of randomly-sized sprites with a random color, random initial position, and random direction

'''
import sys, logging, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
black = (0,0,0)
orange = (255,150,0)
pink = (255, 200, 200)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)
purple = (150, 15, 150)
blue = (0, 40, 255)
indigo = (0, 0, 100)
colorsBlock = [red, orange, pink, dark_green, yellow, purple, blue, indigo]

class Block(pygame.sprite.Sprite):
        def __init__(self, color, size, position, direction):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface(size)
                self.image.fill(color)
                self.rect = self.image.get_rect()
                (self.rect.x,self.rect.y) = position
                self.direction = direction

        def update(self):
                (dx,dy) = self.direction
                self.rect.x += dx
                self.rect.y += dy
                (WIDTH,HEIGHT) = screen_size
                if self.rect.left > WIDTH:
                        self.rect.right = 0
                if self.rect.right < 0:
                        self.rect.left = WIDTH
                if self.rect.top > HEIGHT:
                        self.rect.bottom = 0
                if self.rect.bottom < 0:
                        self.rect.top = HEIGHT


def main():
        pygame.init()
        screen = pygame.display.set_mode(screen_size)
        clock = pygame.time.Clock()

        blocks = pygame.sprite.Group()
        for i in range(1, random.randint(1,100)):
                block = Block(random.choice(colorsBlock),(random.randint(1,100),random.randint(1,100)),(random.randint(1,700),random.randint(1,500)),(random.randint(-10,10),random.randint(-10,10)))
                blocks.add(block)

        while True:
                clock.tick(FPS)
                screen.fill(black)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)

                blocks.update()
                blocks.draw(screen)
                pygame.display.flip()

if __name__ == '__main__':
        main()
