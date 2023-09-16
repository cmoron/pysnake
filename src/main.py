#!/usr/bin/env python3

"""
Ce module est le point d'entrée pour le jeu Snake.
Il gère la logique du jeu, l'entrée de l'utilisateur et le rendu à l'écran.
"""

import pygame
from snake import Snake
from food import Food

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

# Configuration du taux de rafraîchissement
clock = pygame.time.Clock()

# Création des objets Snake et Food
snake = Snake()
food = Food()

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # Changement de direction sur la pression des touches
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    # Logique du jeu
    food_position = food.spawn_food()
    if snake.move(food_position):
        food.set_food_on_screen(False)

    # Rendu graphique
    window.fill(pygame.Color(0, 0, 0))

    # Dessin du serpent
    for pos in snake.get_body():
        pygame.draw.rect(window, pygame.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Dessin de la nourriture
    pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(food_position[0],
                                                                  food_position[1], 10, 10))

    # Vérification des collisions
    if snake.check_collision():
        print("Colision ! ")
        pygame.quit()

    # Actualisation de l'écran
    pygame.display.flip()

    # Taux de rafraîchissement
    clock.tick(240)
