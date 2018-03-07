#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL)
# Sets the level for when the user is warned about a bug to critical.
logger = logging.getLogger(__name__)
# Initializes a logger object

screen_size = (800,600)
# Sets a screen size as a tuple, for later use in pygame
FPS = 60
# FPS is set to 60 for pygame
red = (255,0,0)
# Creates a tuple for the color red in RGB
black = (0,0,0)
# Same as above but for black.

class Block(pygame.sprite.Sprite):
        #A class definition for Block.
	def __init__(self, position, direction):
                # A magic method for initializing the class.
		pygame.sprite.Sprite.__init__(self)
		#Calls the sprite class and initializes that as well.
		self.image = pygame.Surface((50, 50))
		# the surface to display an image. I imagine this is from the Sprite class.
		self.image.fill(red)
		# Fills the image with red.
		self.rect = self.image.get_rect()
		# Calls a method to make a rectangle.
		(self.rect.x,self.rect.y) = position
		# Creates a starting position
		self.direction = direction
		# Creates a direction for the block to go.

	def update(self):
		(dx,dy) = self.direction
		# records the direction of x and y. Technically records the speeds in x and y seperately, like velocity in physics.
		self.rect.x += dx
		# changes the x position using the x velocity.
		self.rect.y += dy
		# Changes the y position using the y velocity.
		(WIDTH,HEIGHT) = screen_size
		# This and the next 8 lines are used to move the square to the other side once it leaves the screen
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
	# Initializes Pygame
	screen = pygame.display.set_mode(screen_size)
        # sets the screen size to the earlier tuple
	clock = pygame.time.Clock()
	# initializes a clock object

	blocks = pygame.sprite.Group()
	# initializes blocks as a sprite group
	block = Block((200,200),(-1,1))
	# initializes block as a block
	blocks.add(block)
	# adds block to the sprite group Blocks

	while True:
		clock.tick(FPS)
		# runs the game at FPS
		screen.fill(black)
		# Makes the screen black

		for event in pygame.event.get():
                        # Checks events and only checks for quitting using the red x.
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

		blocks.update()
		# Updates the blocks object
		blocks.draw(screen)
		# draws using the Sprite class
		pygame.display.flip()
		# updates the screen

if __name__ == '__main__':
	main()
