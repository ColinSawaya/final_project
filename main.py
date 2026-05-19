#imports
import pygame

from Bird import Bird
from Pipe import Pipe
from pygame import mixer

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
SCORE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
END_SCREEN_COLOR = (255, 0, 0)

#Frames per second
FPS = 30

#set up screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_img = pygame.image.load("./images/background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

#sounds
jump_sound = pygame.mixer.Sound("./sounds/swoosh.mp3")
jump_sound.set_volume(0.3)
score_sound = pygame.mixer.Sound("./sounds/plus_one.mp3")
score_sound.set_volume(0.5)
game_over_sound = pygame.mixer.Sound("./sounds/game_over_sound.mp3")
game_over_sound.set_volume(0.3)


#font
font = pygame.font.SysFont('arial', 22)
pygame.display.set_caption("Flappy Bird by Colin Sawaya")

#create a clock
clock = pygame.time.Clock()

def main(): #the game loops
    running = True
    game_over = False
    saved = False
    bird = Bird(screen, BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_JUMP_STRENGTH)
    pipe = Pipe(screen, WIDTH, PIPE_WIDTH, GAP_HEIGHT, PIPE_SPEED, PIPE_COLOR, HEIGHT)

    score = 0
    file = open("high_score.txt")
    high_score = int(file.read())
    file.close()
    
    while running:
        clock.tick(FPS)
        screen.blit(background_img, (0, 0))


        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    jump_sound.play()
                if event.key == pygame.K_r and game_over:
                    bird = Bird(screen, BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_JUMP_STRENGTH)
                    pipe = Pipe(screen, WIDTH, PIPE_WIDTH, GAP_HEIGHT, PIPE_SPEED, PIPE_COLOR, HEIGHT)
                    score = 0
                    game_over = False
                if event.key == pygame.K_ESCAPE:
                    running = False
        if bird.y > HEIGHT:
            game_over = True

        if pipe.off_screen():
            pipe.reset()

        if not game_over:
            bird.move()
            pipe.move()
        

        if bird.y < 0:
            bird.y = 0
            bird.velocity = 0

        if pipe.x + pipe.width == bird.x:
            score += 1
            score_sound.play()

        if score > high_score:
            high_score = score


        if bird.x < pipe.x + pipe.width and bird.x + bird.size > pipe.x:
            if bird.y < pipe.gap_y or bird.y + bird.size > pipe.gap_y + pipe.gap_height:
                game_over = True

        pipe.draw()
        bird.draw()

        score_text = f"Score: {score}"
        text_surface = font.render(score_text, True, SCORE_COLOR)
        screen.blit(text_surface, (WIDTH // 2, 20))

        high_text = font.render(f"High Score: {high_score}", True, SCORE_COLOR)
        screen.blit(high_text, (WIDTH // 2, 50))

        if game_over:
            game_over_text = font.render("GAME OVER - Press R to Restart and Esc to Quit", True, END_SCREEN_COLOR)
            high_score_text = font.render(f"Your score was {score}", True, END_SCREEN_COLOR)
            screen.blit(game_over_text, (180, HEIGHT // 2))
            screen.blit(high_score_text, (180, HEIGHT // 2 - 50))
            
        if game_over and not saved:
            file = open("high_score.txt", "w")
            file.write(str(high_score))
            file.close()
            saved = True
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    