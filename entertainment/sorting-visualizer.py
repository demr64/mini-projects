import pygame
import numpy as np
from numpy import ndarray

pygame.init()
pygame.font.init()

# window size
screen = pygame.display.set_mode((850, 600))

pygame.display.set_caption("Sorting algorithms")

bar_breadth = 15

list_capacity = 25
random_list = np.random.randint(15, 200, list_capacity)
x = 50
y = 475
running = True
rect_rgb = (50,50,50)
font = pygame.font.SysFont(None, 24)
img = font.render('Sorting visualizer', False, (0, 0, 0))
img2 = font.render('Press numbers in order from [1,...5] for:', False, (0, 0, 0))
img3 = font.render('Bubble S., Insertion S., Selection S., Merge S., Heap S.', False, (0, 0, 0))
support = [0] * (len(random_list))


def show(lst):
    for i in range(len(lst)):
        pygame.draw.rect(screen, rect_rgb, (x + 30 * i, y - lst[i], bar_breadth, lst[i]))


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def update_screen():
    screen.fill((90, 160, 140))
    show(random_list)
    pygame.time.delay(45)
    screen.blit(img, (20, 20))
    screen.blit(img2, (20, 50))
    screen.blit(img3, (20, 80))
    pygame.display.update()


def quit():
    pygame.time.delay(100)
    pygame.quit()


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
                update_screen()


def insertion_sort(lst):
    for i in range(len(lst) - 1):
        while lst[i] > lst[i + 1] and i >= 0:
            swap(lst, i, i + 1)
            i = i - 1
            update_screen()


def selection_sort(lst):
    mn = 1e9
    cnt = 0
    for i in range(len(lst) - 1):
        mn = lst[i]
        cnt = i
        for j in range(i + 1, len(lst)):
            if mn > lst[j]:
                cnt = j
                mn = lst[j]

        swap(lst, i, cnt)
        update_screen()


def merge(lst, left, mid, right):
    i = left
    h = left
    j = mid + 1
    while i <= mid and j <= right:
        if lst[i] > lst[j]:
            support[h] = lst[j]
            j += 1
        elif lst[j] >= lst[i]:
            support[h] = lst[i]
            i += 1
        h += 1
    j = 0
    while i <= mid:
        lst[right - j] = lst[mid - j]
        i += 1
        j += 1

    for m in range(left, h):
        lst[m] = support[m]
    update_screen()


def merge_sort(lst, left, right):
    if left >= right:
        return
    mid = left + (right - left) // 2
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)
    merge(lst, left, mid, right)


def cn(random_list):
    random_list = np.random.randint(15, 200, list_capacity)
    pygame.time.delay(1000)
    update_screen()


while running:
    execute = False
    run = True
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # if the action is to quit
        if keys[pygame.K_0]:
            quit()
        screen.fill((200,200,200))
        show(random_list)
        pygame.display.update()
        # command for sorting is executed
        if keys[pygame.K_1]:
            bubble_sort(random_list)
            random_list = np.random.randint(15, 200, list_capacity)
            pygame.time.delay(1000)
            update_screen()

        elif keys[pygame.K_2]:
            insertion_sort(random_list)
            random_list = np.random.randint(15, 200, list_capacity)
            pygame.time.delay(1000)
            update_screen()

        elif keys[pygame.K_3]:
            selection_sort(random_list)
            random_list = np.random.randint(15, 200, list_capacity)
            pygame.time.delay(1000)
            update_screen()

        elif keys[pygame.K_4]:
            merge_sort(random_list, 0, len(random_list) - 1)

        pygame.display.update()

    screen.fill((200,200,200))
    show(random_list)
    screen.blit(img, (20, 20))
    screen.blit(img2, (20, 50))
    screen.blit(img3, (20, 80))
    pygame.display.update()
