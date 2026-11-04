#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques détaillées. 
- ***Cet exercice s'inspire largement d'un TP construit par Christian Vercauter, enseignant d'informatique à l'Ecole Centrale de Lille, aujoud'hui retraité.***
- Le programme doit afficher en plus des informations précédentes du programme comptage : 
    - Le nombre total de caractères alphabétiques rencontrés. 
    - Un tableau présentant le nombre d'occurrences de chaque caractère alphabétique, ainsi que sa fréquence (rapport entre le nombre d'occurrences d'un caractère alphabétique sur le nombre total de caractères alphabétiques).
- **Indications** : Créer et initialiser à zéro, une liste de 29 composantes entières, qui contiendra les occurrences des caractères alphabétiques mais également le nombre total de mots, lignes, caractères et caractères alphabétiques rencontrés. 
- Considérer les caractères accentués de manière spéficique à l'aide d'un `match/case`; 
- Tester votre programme sur les deux extraits du roman de Georges Perec (1936-1982) intitulé "La Disparition" paru en 1969. Que remarquez-vous en examinant les résultats ?
- Tester votre programme sur l'extrait d'un autre roman de Georges Perec, intitulé "Les Revenentes" paru en 1972. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **lipogramme** ?
- Tester votre programme sur le texte suivant : *"Portez ce vieux whisky au juge blond qui fume"*. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **pangramme** ? A quoi servent les pangrammes en informatique ?
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 
"""
import os
import sys


def normaliser_accent(c):
  """Remplace un caractère accentué par son équivalent sans accent."""
  match c:
    case "à" | "â" | "ä":
      return "a"
    case "é" | "è" | "ê" | "ë":
      return "e"
    case "î" | "ï":
      return "i"
    case "ô" | "ö":
      return "o"
    case "ù" | "û" | "ü":
      return "u"
    case "ç":
      return "c"
    case _:
      return c

def lire():
    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        texte = f.read()
        f.close()
    else:
        texte = sys.stdin.read()

  # 2. Initialisation des 30 compteurs à 0
  # Indices 0 à 25 : lettres 'a' à 'z'
  # Indice 26 : lignes | 27 : mots | 28 : caractères totaux | 29 : caractères alphabétiques
    stats = [0] * 30
    dans_un_mot = False

  # 3. Parcours du texte
    for c in texte:
        stats[28] += 1  # Caractères totaux

        # Le match DOIT être indenté ici (dans la boucle)
        match c:
            case "\n":
                stats[26] += 1  # Lignes
                dans_un_mot = False
            case " " | "\t":
                dans_un_mot = False
            case _:
                if not dans_un_mot:
                    stats[27] += 1  # Mots
                    dans_un_mot = True

        # Le traitement alphabétique DOIT aussi être dans la boucle
        c_base = normaliser_accent(c.lower())
        if "a" <= c_base <= "z":
            stats[29] += 1  # Caractères alphabétiques
            indice = ord(c_base) - ord("a")
            stats[indice] += 1

  # 4. Affichage des caractéristiques générales
    print(f"Lignes : {stats[26]}")
    print(f"Mots : {stats[27]}")
    print(f"Caractères totaux : {stats[28]}")
    print(f"Caractères alphabétiques : {stats[29]}")
    print("\n--- Fréquence des lettres ---")

    total_alpha = stats[29]

  # 5. Affichage du tableau d'occurrences et fréquences
    for i in range(26):
        lettre = chr(ord("a") + i)
        occurrences = stats[i]
        frequence = (occurrences / total_alpha) if total_alpha > 0 else 0.0
        print(f"{lettre} : {occurrences:5d}  ({frequence * 100:6.2f} %)")


if __name__ == "__main__":
    lire()
