#imports
import pygame
from Bird import Bird
from Pipe import Pipe

#SCREEN CONSTANTS
WIDTH = 800
HEIGHT = 600

#BIRD CONSTANTS
BIRD_X = 200
BIRD_Y = 300
BIRD_SIZE = 30
BIRD_FALL_SPEED = 4
BIRD_JUMP_STRENGTH = 18

#PIPE CONSTANTS
PIPE_WIDTH = 50
PIPE_SPEED = 5
GAP_HEIGHT = 150
PIPE_COLOR = (0, 255, 0)

# COLOR CONSTANTS
BIRD_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

#set up screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#Frames per second
FPS = 30

#font
font = pygame.font.SysFont('arial', 22)
pygame.display.set_caption("Flappy Bird by Colin Sawaya")

#create a clock
clock = pygame.time.Clock()

def main(): #the game loops
    running = True
    bird = Bird(screen, BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_JUMP_STRENGTH, BIRD_COLOR)
    pipe = Pipe(screen, WIDTH, PIPE_WIDTH, GAP_HEIGHT, PIPE_SPEED, PIPE_COLOR, HEIGHT)

    score = 0

    
    while running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)


        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        if bird.y > HEIGHT:
            running = False

        if pipe.off_screen():
            pipe.reset()
        bird.move()
        pipe.move()
        if bird.y < 0:
            bird.y = 0
            bird.velocity = 0

        if bird.x < pipe.x + pipe.width and bird.x + bird.size > pipe.x:
            if bird.y < pipe.gap_y or bird.y + bird.size > pipe.gap_y + pipe.gap_height:
                running = False

        pipe.draw()
        bird.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()