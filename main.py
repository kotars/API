import os
import sys
import pygame
import requests


def map2(x, y, z, l):
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&l={l}&z={z}"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.jfif"
    with open(map_file, "wb") as file:
        file.write(response.content)


x = 37.620070
y = 55.753630
z = 8
l = "map"
map2(x, y, z, l)
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
        result = pygame.key.get_pressed()
        if result[pygame.K_PAGEUP]:
            if z < 17:
                z += 1
        if result[pygame.K_PAGEDOWN]:
            if z > 2:
                z -= 1
        if result[pygame.K_LEFT]:
            x -= 0.001
        if result[pygame.K_RIGHT]:
            x += 0.001
        if result[pygame.K_UP]:
            if y < 180:
                y += 0.001
        if result[pygame.K_DOWN]:
            if y > 0:
                y -= 0.001
        if result[pygame.K_1]:
            l = 'map'
        if result[pygame.K_2]:
            l = 'sat'
        if result[pygame.K_3]:
            l = 'sat,skl'
    map2(x, y, z, l)
    map_file = "map.jfif"
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
