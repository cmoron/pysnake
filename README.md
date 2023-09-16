# PySnake

Un simple jeu Snake développé en Python en utilisant la bibliothèque Pygame.

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Caractéristiques](#caractéristiques)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/your_username/PySnake.git
    ```

2. Installez les dépendances :

    ```bash
    cd PySnake
    pip install -r requirements.txt
    ```

## Utilisation

Après avoir installé les dépendances, exécutez le script `main.py` :

```bash
python src/main.py
```

Utilisez les touches fléchées pour contrôler le serpent. Collectez de la nourriture pour augmenter la taille du serpent. Le jeu se termine lorsque le serpent entre en collision avec lui-même ou avec les murs de l'aire de jeu.

## Structure du projet

- `src/`: Dossier contenant le code source
  - `main.py`: Point d'entrée du jeu
  - `snake.py`: Classe pour gérer le serpent
  - `food.py`: Classe pour gérer la nourriture
- `assets/`: Dossiers contenant les fichiers image, son, etc.
- `requirements.txt`: Fichier contenant les dépendances du projet

## Caractéristiques

- Interface utilisateur simple
- Détection de collision
- Score en temps réel
- Nourriture aléatoire

## Contribuer

Si vous souhaitez contribuer à ce projet, merci de créer une "pull request" ou de signaler les problèmes que vous trouvez.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
