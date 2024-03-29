import pygame
import Paddle from models
import Ball from models
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Frames Per Second - Game Speed
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7
        

def draw(win, paddles, ball):
    win.fill(BLACK)
    for paddle in paddles:
        paddle.draw(win)  
        
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue  
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
        
        
    ball.draw(win)
    pygame.display.update()
    
    
def deflect_ball_collision(ball, paddle):
    middle_y = paddle.y + paddle.height / 2
    difference_in_y = middle_y - ball.y
    reduction_factor = (paddle.height / 2) / ball.MAX_VEL
    y_vel = difference_in_y / reduction_factor
    ball.y_vel = -1 * y_vel
    
    
   
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                 ball.x_vel *= -1
                 deflect_ball_collision(ball, left_paddle)
    else:  
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                deflect_ball_collision(ball, right_paddle)
    
    
def handle_paddle_movement(keys, left_paddle, right_paddle):
    # move left paddle
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
        
    # move right paddle
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()
    
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
    
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the user clicks the exit button
                run = False
                break
            
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)   
        ball.move() 
        handle_collision(ball, left_paddle, right_paddle)
            
    pygame.quit()
 
if __name__ == '__main__':
    main() 