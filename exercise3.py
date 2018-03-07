#!/usr/bin/env python
'''

For this exercise, create random sprites from images, rather than blocks of color

You will need to find or create images for this purpose; https://opengameart.org may be a good resource for you

'''
import sys, logging, pygame, random, os
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)

cwd = str(os.getcwd())

directory = cwd + "\last-guardian-sprites"

images = os.listdir(directory)

class Block(pygame.sprite.Sprite):
        def __init__(self, img, position, direction):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(str(img)).convert()
                self.rect = self.image.get_rect()
                self.image.set_colorkey(white)
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
                block = Block(directory + "\\" + str(random.choice(images)),(200,200),(random.randint(-10,10), random.randint(-10,10)))
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
