import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Frames Per Second - Game Speed
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20 

class Paddle:
    COLOR = WHITE
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rectangle(win, set.COLOR, (self.x, self.y, self.width, self.height))
        

def draw(win):
    win.fill(WHITE)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    while run:
        clock.tick(FPS)
        draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the user clicks the exit button
                run = False
                break
            
    pygame.quit()
 
if __name__ == '__main__':
    main()