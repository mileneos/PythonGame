import pygame
import random
import time
WINDOW_SIZE = [500, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()


def printtext(message, x, y, color=(0, 0, 0), type="8277.ttf", size=30):
    type = pygame.font.Font(type, size)
    text = type.render(message, True, color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, width, height, color1, color2):
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2

    def draw(self, x, y, message, active=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x < mouse[0] < x + self.width) and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, GREEN, (x, y, self.width, self.height))
            if click[0] == 1:
                if active is not None:
                    active()
        else:
            pygame.draw.rect(screen, RED, (x, y, self.width, self.height))
        printtext(message, x + 60, y + 20)


def show_menu():
    pygame.display.set_mode(WINDOW_SIZE)
    menu_show = True
    start = Button(300, 70, GREEN, RED)
    while menu_show:
        screen.fill(BLACK)
        start.draw(110, 180, "START GAME", rungame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()


def rungame():
    start_time = time.perf_counter()
    a1 = random.randint(0, 4)
    b1 = random.randint(0, 4)
    score = 0
    WIDTH = 40
    HEIGHT = 40
    MARGIN = 14
    grid = []
    for row in range(5):
        grid.append([])
        for column in range(5):
            grid[row].append(0)
    pygame.display.set_caption("Проверь свою реакцию!")
    done = False
    printtext("SCORE :" + str(score), 350, 100, GREEN)
    clock = pygame.time.Clock()
    while not done:
        screen.fill(BLACK)
        printtext("Цель: 25", 350, 30, GREEN)
        printtext("Счёт:" + str(score), 350, 100, GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if column < 5 and row < 5:
                    grid[row][column] = 1
                    print("Click ", row, column)
        for row in range(5):
            for column in range(5):
                color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * b1 + MARGIN,
                                  (MARGIN + HEIGHT) * a1 + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        if grid[a1][b1] == 1:
            score += 1
            print(score)
            a1 = random.randint(0, 4)
            b1 = random.randint(0, 4)
            grid[a1][b1] = 0
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * b1 + MARGIN,
                              (MARGIN + HEIGHT) * a1 + MARGIN,
                              WIDTH,
                              HEIGHT])

        if score == 25:
            res = int(time.perf_counter() - start_time)
            done = True
            end(res)
        clock.tick(60)
        pygame.display.flip()


def end(x):
    res = x
    pygame.display.set_mode(WINDOW_SIZE)
    menu_show = True
    restart = Button(230, 70, GREEN, RED)
    while menu_show:
        screen.fill(BLACK)
        printtext("Ваше время - " + str(res) + "c", 150, 100, WHITE)
        if res <= 10:
            printtext("Вы киберспортсмен!", 120, 140, WHITE)
        elif res <= 15:
            printtext("Всё в норме!", 185, 140, WHITE)
        else:
            printtext("Вы стареете!", 180, 140, WHITE)
        restart.draw(140, 200, "RESTART",rungame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()


show_menu()


