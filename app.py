import pygame
import math
import random
import time

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sorting Visualizer")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def random_list():
    random_number = random.randint(30,50)
    r_list = random.sample(range(10,300), random_number)
    return r_list

def draw(win, color, x, y, width, height):
    return pygame.draw.rect(win, color, (x,y,width, height))

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst



def main():
    run = True
    lst = random_list()
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(TURQUOISE)
        width = WIDTH/len(lst)
        for i in range(len(lst)):
            draw(WIN, ORANGE, i*width, WIDTH-lst[i], width, lst[i])
        pygame.display.update()
        # time.sleep(3)
        for i in range(len(lst)-1):
            for j in range(0,len(lst)-i-1):
                draw(WIN, ORANGE, i*width, WIDTH-lst[i], width, lst[i])
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    
                    time.sleep(.1)
                    # clock.tick(300)
                    pygame.display.update()

        # new_lst = bubble_sort(lst)
        # for i in range(len(new_lst)):
        #     draw(WIN, ORANGE, i*width, WIDTH-new_lst[i], width, new_lst[i])
        # pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
    # print(bubble_sort([7,4,9,2,0,1]))
