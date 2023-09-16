"""
Ce module contient la classe Snake qui représente le serpent dans le jeu Snake.
"""

class Snake:
    """
    Classe représentant le serpent dans le jeu Snake.
    """
    def __init__(self):
        """
        Constructeur de la classe Snake.
        Initialise la position du serpent et sa direction.
        """
        self.position = [100, 50]  # Position de la tête du serpent
        self.body = [[100, 50], [90, 50], [80, 50]]  # Corps du serpent
        self.direction = "RIGHT"  # Direction initiale du serpent

    def change_direction(self, new_direction):
        """
        Change la direction du serpent.

        :param new_direction: La nouvelle direction ("UP", "DOWN", "LEFT", "RIGHT")
        """
        # Vérification pour éviter que le serpent ne puisse pas aller
        # dans la direction opposée à celle actuelle
        if new_direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if new_direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if new_direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if new_direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_position):
        """
        Déplace le serpent en fonction de la direction.

        :param food_position: Position de la nourriture
        :return: True si le serpent a mangé la nourriture, sinon False
        """
        # Mettre à jour la position de la tête du serpent en fonction de la direction
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        # Ajouter la nouvelle position de la tête à l'avant du corps
        self.body.insert(0, list(self.position))

        # Vérifier si le serpent a mangé la nourriture
        if self.position == food_position:
            return True
        # Retirer le dernier élément du corps, car le serpent n'a pas mangé de nourriture
        self.body.pop()
        return False

    def check_collision(self):
        """
        Vérifie si le serpent est entré en collision avec les bords de l'écran ou lui-même.

        :return: True si collision, sinon False
        """
        # Vérification des collisions avec les bords de l'écran
        if self.position[0] >= 800 or self.position[0] <= 0 or \
           self.position[1] >= 600 or self.position[1] <= 0:
            return True
        # Vérification des collisions avec lui-même
        for segment in self.body[1:]:
            if segment == self.position:
                return True
        return False

    def get_head_position(self):
        """
        Retourne la position de la tête du serpent.

        :return: Position de la tête du serpent
        """
        return self.position

    def get_body(self):
        """
        Retourne le corps du serpent.

        :return: Corps du serpent
        """
        return self.body
