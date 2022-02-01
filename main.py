import os
import sys
import pygame
import requests


x = float(input())
y = float(input())
map_request = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=20,20&l=sat"
response = requests.get(map_request)


if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)


map_file = "map.jfif"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
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


pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)