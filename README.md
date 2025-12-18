# Voici le repo du rendu de projet de POO du groupe Les Potes Âgés

## Sommaire
- [Chronobio](#chronobio)
- [Install](#install)
    - [Installation de l'environement](#installation-de-lenvironement)
    - [Installation du jeu](#installation-du-jeu)
- [Lancer le jeux](#lancer-le-jeux)
- [Tests](#tests)
- [Structure du projet](#structure-du-projet)
- [Contributeur](#contributeur)

## Chronobio
Chronobio est un jeu de programmation pour gérer une ferme, produire des légumes, les vendre, faire des coupe et devenir le meilleur producteur de légume dans un environnement concurrentiel et dynamique.


## Install 

```
py -3.13 -m venv venv
```
```
.\venv\Scripts\Activate.ps1
```
```
python -m pip install --upgrade pip chronobio "chronobio[dev]"
```
```
.\venv\Scripts\python.exe -m chronobio.game.server -p 12345
```
```
.\venv\Scripts\python.exe -m chronobio.viewer -p 12345
```
```
.\venv\Scripts\python.exe -m '"nom de notre progrmme.PY' -p 12345
```
``pour léo : cd C:\Users\admin\PyCharmMiscProject``


### Installation de l'environement

```powershell
# Créer et activer un environnement virtuel
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
```

### Installation du jeu

```python
python -m pip install --upgrade pip chronobio "chronobio[dev]"
```

## Lancer le jeux

Pour lancer le projet, il faut lancer le fichier **launcher.py**.

## Tests
Pour testé les code.

## Structure du projet
```
Projet-POO-M1/
├── tests/              # Tests Unitaires
│ ├── init.py
│ └── test_player.py
├── .gitignore          # Git Ignore
├── my_farm.txt         # Json Model
├── README.md           # Doc
└── main.py             # Programme
```
`` en dév -bloucle.py et -local_base.py ``


## Contributeur

- Guillaume LANDFROID-NAZAC 
- Mathis DÉRONNE
- Damien ZORZETTO
- Leo TISSOT
- Edwin LE ROYER


## Règles et sources

https://github.com/vpoulailleau/chronobio