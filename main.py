import os
import sys
import pygame
import requests


def map2(x, y, z=8):
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&l=sat&z={z}"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.jfif"
    with open(map_file, "wb") as file:
        file.write(response.content)


x = float(input())
y = float(input())
z = 8
map2(x, y, z)
map_file = "map.jfif"
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if z < 17:
                z += 1
            map2(x, y, z)
        if event.type == pygame.KEYDOWN:
            if z > 0:
                z -= 1
            map2(x, y, z)
    map_file = "map.jfif"
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    clock.tick(50)

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
