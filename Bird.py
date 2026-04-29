class Bird:
    def __init__(self, screen, x, y, size, fall_speed, jump_strength, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.fall_speed = fall_speed
        self.jump_strength = jump_strength
        self.color = color
        self.velocity = 0
    
    def move(self):
        self.y += fall_speed #keeps it going down

    def jump(self):
        self.y -= self.jump_strength #upward movement
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color,(self.x, self.y, self.size, self.size))