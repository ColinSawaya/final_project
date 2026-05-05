#imports
import pygame
import random

class Pipe():
    def __init__(self, screen, x, width, gap_height, speed, color, screen_height):
        self.screen = screen
        self.x = x
        self.width = width
        self.gap_height = gap_height
        self.speed = speed
        self.color = color
        self.screen_height = screen_height

        self.gap_y = random.randint(100, screen_height - 100 - gap_height)
    
    def move(self):
        self.x -= self.speed

    def draw(self):
        #top pipee
        pygame.draw.rect(self.screen, self.color, (self.x, 0, self.width, self.gap_y))
        #bottom pipe
        pygame.draw.rect(self.screen, self.color, (self.x, self.gap_y + self.gap_height, self.width, self.screen_height))

    def off_screen(self):
        return self.x < -self.width
    
    def reset(self):
        self.x = 800  # or WIDTH constant
        self.gap_y = random.randint(100, self.screen_height - 100 - self.gap_height)
        