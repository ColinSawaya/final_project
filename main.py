#imports
import pygame
from Bird import Bird


#SCREEN CONSTANTS
WIDTH = 800
HEIGHT = 600

#BIRD CONSTANTS
BIRD_X = 200
BIRD_Y = 300
BIRD_SIZE = 30
BIRD_FALL_SPEED = 4
BIRD_JUMP_STRENGTH = 50

# COLOR CONSTANTS
BIRD_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

#set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

#Frames per second
FPS = 30

#font
font = pygame.font.SysFont('arial', 22)
pygame.display.set_caption("Flappy Bird by Colin Sawaya")

#create a clock
clock = pygame.time.Clock()

def main(): #the game loops
    running = True
    bird = Bird(screen, BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_FALL_SPEED, BIRD_JUMP_STRENGTH, BIRD_COLOR)
    score = 0

    clock.tick(FPS)
    while running:
        screen.fill(BACKGROUND_COLOR)


        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                running = False


if __name__ == "__main__":
    main()
    pygame.quit()