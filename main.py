import pygame
import sys
from pygame import Vector2
import random
import time as t
class Ball:
    def __init__(self):
        self.x = 3
        self.y = 3
        self.pos = Vector2(screen_width // 2 - 10, screen_height // 2 - 10)
        self.ball_rect = pygame.Rect(self.pos.x,self.pos.y, 20, 20)
    def draw_ball(self):
        pygame.draw.ellipse(screen, (255, 0, 0), self.ball_rect)

    def ball_move(self):
        self.ball_rect.x += self.x
        self.ball_rect.y += self.y
    def restart(self):
        self.ball_rect.center =(screen_width//2, screen_height //2)
        self.x *= random.choice((1, -1))
        self.y *= random.choice((1, -1))
        t.sleep(0.1)

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game by revanth")
time = pygame.time.Clock()

player1 = pygame.Rect(screen_width-20 , screen_height//2-50 ,10, 100)
player2 = pygame.Rect(10, screen_height//2-50, 10, 100)
player1_speed = 0
player2_speed = 0

l_score = 0
r_score = 0
ball = Ball()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 5
            if event.key == pygame.K_UP:
                player1_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 5
            if event.key == pygame.K_UP:
                player1_speed += 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player2_speed += 5
            if event.key == pygame.K_w:
                player2_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player2_speed -= 5
            if event.key == pygame.K_w:
                player2_speed += 5


    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

    ball.ball_move()
    player1.y += player1_speed
    player2.y += player2_speed
    screen.fill((0, 0, 0))
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.circle(screen,(255, 255, 255),(screen_width//2, screen_height//2),100, 1)
    ball.draw_ball()
    pygame.draw.rect(screen,(0, 255, 0), player1)
    pygame.draw.rect(screen,(0, 255, 0), player2)
    if ball.ball_rect.top <= 0 or ball.ball_rect.bottom >= screen_height:
        ball.y *= -1
    if ball.ball_rect.left < 0 :
        ball.restart()
        r_score += 1
    if ball.ball_rect.right > screen_width:
        ball.restart()
        l_score += 1

    if ball.ball_rect.colliderect(player1) or ball.ball_rect.colliderect(player2):
        ball.x *=-1

    font1 = pygame.font.SysFont("comicsansms", 20)
    label1 = font1.render("Sore "+ str(l_score), True, (255, 255, 0))
    screen.blit(label1, (50, 20))

    font2 = pygame.font.SysFont("comicsansms", 20)
    label2 = font2.render("Sore " + str(r_score), True, (255, 255, 0))
    screen.blit(label2, (570, 20))
    if r_score == 10:
        screen.fill(pygame.Color('black'))
        font1 = pygame.font.SysFont("comicsansms", 30)
        label1 = font1.render("Player2 has Won", True, (255, 255, 0))
        screen.blit(label1, (screen_width//2 - 100, screen_height//2-10 ))

    if l_score == 10:
        screen.fill(pygame.Color('black'))
        font1 = pygame.font.SysFont("comicsansms", 30)
        label1 = font1.render("Player1 has Won", True, (255, 255, 0))
        screen.blit(label1, (screen_width // 2 - 100, screen_height // 2 - 10))

    pygame.display.flip()
    time.tick(60)
