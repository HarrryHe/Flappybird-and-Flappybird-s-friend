import pygame
import random
import os

W, H = 288, 512

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("FlappyBirds and FlappyBirds' friends")
clock = pygame.time.Clock()

images = {}
for image in os.listdir("assets/sprites"):
    name, extension = os.path.splitext(image)
    path = os.path.join('assets/sprites', image)
    images[name] = pygame.image.load(path)

floor_y = H - images['floor'].get_height()
start = pygame.mixer.Sound('assets/audio/start.wav')
die = pygame.mixer.Sound('assets/audio/die.wav')
hit = pygame.mixer.Sound('assets/audio/hit.wav')
score_x = pygame.mixer.Sound('assets/audio/score.wav')
flap_audio = pygame.mixer.Sound('assets/audio/flap.wav')

def main():

    while True:
        start.play()
        images['background'] = images[random.choice(['day', 'night', 'ice', 'rock', 'sky', 'green', 'rocky'])]
        images['birds'] = images[random.choice(['girl-1', 'girl-2', 'slime', 'tomato', 'dragon', 'doraemon', 'red-mid', 'yellow-mid', 'blue-mid', 'red-up', 'yellow-up', 'blue-up', 'red-down', 'yellow-down', 'blue-down'])]
        images['pipes'] = images[random.choice(['green-pipe', 'red-pipe'])]

        menu_window()
        result = game_window()
        end_window(result)

def menu_window():

    floor_gap = images['floor'].get_width() - W
    floor_x = 0

    guide_x = (W - images['guide'].get_width())/2
    guide_y = (floor_y - images['guide'].get_height())/2

    bird_x = W * 0.2
    bird_y = (H - images['birds'].get_height())/2
    bird_y_vel = 1
    bird_y_range = [bird_y - 8, bird_y + 8]



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        floor_x -= 4
        if floor_x <= - floor_gap:
            floor_x = 0

        bird_y += bird_y_vel
        if bird_y < bird_y_range[0] or bird_y > bird_y_range[1]:
            bird_y_vel *= -1

        screen.blit(images['background'], (0, 0))
        screen.blit(images['floor'], (floor_x, floor_y))
        screen.blit(images['guide'], (guide_x, guide_y))
        screen.blit(images['birds'], (bird_x, bird_y))
        pygame.display.update()
        clock.tick(45)

