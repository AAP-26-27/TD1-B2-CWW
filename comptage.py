#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

#!/usr/bin/env python3
"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales."""

import os
import sys


def lire():
  # 1. Récupération des arguments et sélection du flux
  if len(sys.argv) > 1:
    fichier = open(sys.argv[1], "r")
    texte = fichier.read()
    fichier.close()
  else:
    texte = sys.stdin.read()

  # 2. Parcours du flux
  nb_caracteres = 0
  nb_lignes = 0
  nb_mots = 0
  dans_un_mot = False
  debug = "DEBUG" in os.environ

  for c in texte:
    nb_caracteres += 1

    match c:
      case "\n":
        nb_lignes += 1
        dans_un_mot = False

      case " " | "\t":
        dans_un_mot = False

      case _:
        # Dès qu'on touche un caractère normal alors qu'on n'était pas dans un mot
        if not dans_un_mot:
          nb_mots += 1
          dans_un_mot = True
          if debug:
            print(f"Mot numéro {nb_mots}", file=sys.stderr)

  # Affichage au format wc : lignes, mots, caractères
  print(f"{nb_lignes}\t{nb_mots}\t{nb_caracteres}")



if __name__ == "__main__":
    lire()
