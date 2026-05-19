import pygame

class Bird:
    def __init__(self, screen, x, y, size, jump_strength):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.jump_strength = jump_strength

        self.velocity = 0
        self.gravity = 1.2

        self.image = pygame.image.load("./images/bird.png")
        self.image = pygame.transform.scale(self.image, (size, size))

    
    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity -= self.jump_strength #upward movement
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))