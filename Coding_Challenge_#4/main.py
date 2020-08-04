import pygame
import random


pygame.init()


purple = (128, 0, 128)
bg_color = (230, 230, 250)
chuvas = []


class Drop:
    def __init__(self):
        self.x = random.randrange(W)
        self.y = random.randint(100, 200)
        self.speed = random.randint(4, 10)

    def fall(self):
        self.y += self.speed
        self.speed += 0.2
        if self.y > H:
            self.y = random.randint(-200, -100)
            self.speed = random.randint(4, 10)

    def draw(self, screen):
        pygame.draw.line(screen, purple,
                         (self.x, self.y),
                         (self.x, self.y + 10),
                         2)


W = 700
H = 700
# Screen settings
screen = pygame.display.set_mode((W, H))
screen.fill(bg_color)


for i in range(500):
    chuvas.append(Drop())


def main():
    Clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(bg_color)
        Clock.tick(60)
        for obj in chuvas:
            obj.draw(screen)
            obj.fall()
        pygame.display.flip()


main()
