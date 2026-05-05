import pygame

class Bird:
    def __init__(self, screen, x, y, size, jump_strength, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.jump_strength = jump_strength
        self.color = color
        self.velocity = 0
        self.gravity = 1.2
    
    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity -= self.jump_strength #upward movement
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color,(self.x, self.y, self.size, self.size))