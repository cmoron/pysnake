"""
Ce module contient la classe Food qui représente la nourriture dans le jeu Snake.
"""

import random

class Food:
    """
    Classe représentant la nourriture dans le jeu Snake.
    """
    def __init__(self):
        """
        Constructeur de la classe Food.
        Initialise la position aléatoire de la nourriture.
        """
        self.position = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]
        self.is_food_on_screen = True

    def spawn_food(self):
        """
        Fait apparaître la nourriture à une position aléatoire.

        :return: Position actuelle de la nourriture
        """
        if not self.is_food_on_screen:
            self.position = [random.randrange(1, 80) * 10, random.randrange(1, 60) * 10]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, choice):
        """
        Définit si la nourriture est actuellement affichée à l'écran ou non.

        :param choice: True si la nourriture est affichée, sinon False
        """
        self.is_food_on_screen = choice
