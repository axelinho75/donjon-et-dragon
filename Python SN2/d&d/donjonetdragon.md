
# 🎲 Projet POO 

Utilisation des concepts de POO du cours Advanced 2, à savoir **les classes, les attributs, les méthodes et l'héritage**

## 🏁 Objectifs

Créer un système de combat dans l'esprit de Donjons & Dragons où 1 à plusieurs **Heros** combattent 1 à plusieurs **Monstre**.

Il faudra donc une classe **Heros** pour créer un héros et une classe **Monstre** pour créer un monstre.

**Heros** et **Monstre** héritent de **Créature**, en effet les 2 ont des choses en communs.

Toute créature possède :
- Un `nom`
- Une `description`
- Des points de vie `pv`
- Une `defense` (CA pour les connaisseurs)
- Une `initiative` (permet de déterminer qui joue en premier)
- Des points de dégats max `degatsMax`
- Un type de dégats (`typeDegats`) parmi la liste suivante
  - Contondant
  - Tranchant
  - Percant
  - Feu
  - Poison
- Une liste d'états `etats` (il pourrait être empoisoné / paralysé / inspiré...)
- Une attaque classique `attaque()` (action d'attaquer qui inflige les dégats de l'attribut `degat`)

Un héros a en plus :
- Une arme
- Un inventaire

Un monstre à en plus :
- Une liste de resistance

Les actions peuvent être de 3 types :
- Attaque (on choisi une cible et essaye de la toucher, en cas de réussite on applique les dégats)
- Soin (on choisi une cible et on applique le soin automatiquement)
- Buff (on choisi une cible et on applique le buff automatiquement)

## Gestion de dés
Le systeme de donjon et dragons se base sur des jet de dés. Il existe des dés à 4, 6, 8, 10, 12 et 20 faces. Un jet de dés est donc un nombre aléatoire entre 1 et la plus grande valeur du dés.

Plusieurs d'action nécéssite des jets de dés :

### Initiative
Au début du combat toutes les créatures *jettent l'initiative* pour savoir qui joue en premier, cela signifie que toute les créature lancent un d20, les meilleurs résultats jouent avant les plus bas

### Attaques
Quand une créature en attaque une autre, elle jette un d20 (dés à 20 faces), si le résultat est supperieur à la defense de la cible cela signifie que l'attaque "touche" la cible, on peut donc lancer un dés pour connaitre les dégats. Le dés des dégats dépend des caracteristique de la créature.

# Déroulement du jeu

Au début du jeu, le joueur choisi le nombre de heros, puis le nombre de monstre. Ensuit il choisi son héros et son arme (qui induira le nombre de dégat et leur type). Toutes les créature lancent l'initiative (voir plus haut) pour savoir dans quelle ordre les créatures joueront.

A chaque tour on affiche le nom de la créature qui joue, et on propose au joueur de choisir ce que fais la créature parmi la liste des actions de celle ci (l'utilisateur saisi un nombre pour éviter les fautes de frappes).

L'utilisateur choisi la cible de l'action (qui peut être la créature elle même), l'action à ainsi un lanceur et une cible. On jette les dés si besoin, et on applique les concéquences attendu.

Si une créature tombe KO (0pv ou moins) elle ne peut plus jouer à son tour. Quand tous les monstres ou tous les heros sont KO le combat s'arrete, on affiche les vainqueurs et on propose à l'utilisateur de rejouer. 


*Optionnel* : Pour ajouter de la complexité au code :
- Le joueur peut saisir certaine caracteristique du héros (`pv`, `dégat` par exemple)
- Le joueur peut changer le nombre de monstres / de héros participant au combat
- Ajouter d'autre options dans le combat à votre guise 



## 🧑‍🏫 Consignes
* Créer une classe **Creature** avec des attributs, des méthodes et un constructeur
* Créer les classes **Heros** et **Monstre**, qui hérite de **Creature**
* Ajouter les spécificités des 2 classes, ajouter un constructeur qui override le constructeur de **Creature**
* Gérer le combat
* Prévoir un cas de victoire et un cas de défaite
* Gérer les erreurs



## ☝ Conseils

Aidez vous du cours.

N'hésitez pas à utiliser la fonction `print()` pour afficher les valeur contenu dans les variables

Prenez le temps de lire les erreurs et essayer de les comprendre avant de les copier-coller bêtement sur internet
