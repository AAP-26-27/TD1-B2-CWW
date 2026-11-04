#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import os
import sys

def arguments():
    """Fonction qui affiche les arguments de la ligne de commande."""
    if len(sys.argv) <= 1:
        print("Erreur : aucun argument fourni.", file=sys.stderr)
        sys.exit(1)

  # 2. Affichage des arguments si la variable DEBUG est active
    if "DEBUG" in os.environ:
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    arguments()         
