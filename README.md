# Projet de POO - Chronobio -

![Coverage](coverage.svg) 

## Groupe : Les Potes Âgés
Ce dépôt contient le rendu du projet de Programmation Orientée Objet (POO) réalisé en M1.

Le projet repose sur le jeu **Chronobio**, un jeu de stratégie automatisé où l'objectif est de gérer une ferme de manière optimale à l'aide de scripts Python.

---

## Sommaire
- [Présentation du projet](#présentation-du-projet)
- [Objectifs](#objectifs)
- [Installation](#installation)
    - [Environnement virtuel](#environnement-virtuel)
    - [Installation de Chronobio](#installation-de-chronobio)
- [Lancement du jeu](#lancement-du-jeu)
- [Stratégie](#stratégie)
- [Tests](#tests)
    - [Installation](#installation-1)
    - [Lancer les tests avec couverture](#lancer-les-tests-avec-couverture)
- [Structure du projet](#structure-du-projet)
- [Contributeurs](#contributeurs)
- [Règles et sources](#règles-et-sources)

---

## Présentation du projet
**Chronobio** est un jeu de programmation dans lequel chaque joueur contrôle une ferme.
Le joueur doit automatiser ses décisions (achat de champs, plantation, gestion des employés, etc.) via un programme Python.

---

## Objectifs

Ce projet avait plusieurs objectifs pédagogiques et techniques.

Il nous a permis de mettre en pratique les concepts fondamentaux de la Programmation Orientée Objet : la séparation des responsabilités, la factorisation et l’écriture de tests unitaires.

Nous devions également concevoir une architecture de projet claire, lisible et maintenable, capable d’évoluer facilement. Le travail en équipe sur un même dépôt Git faisait partie intégrante du projet : organisation, répartition des tâches, gestion des versions et coordination du code.

L’objectif était aussi d’automatiser une stratégie de jeu à l’aide de scripts Python et de garantir la fiabilité du programme grâce à une suite de tests avec mesure de couverture.

Ce projet nous a surtout permis de passer d’une compréhension théorique de la POO à une mise en œuvre concrète dans un cas pratique proche d’un projet réel, tout en développant notre capacité à travailler en équipe.

---

## Installation
### Environnement virtuel
```powershell
py -3.13 -m venv venv
.\venv\Scripts\Activate.ps1
```

### Installation de Chronobio
```powershell
python -m pip install --upgrade pip 
python -m pip install chronobio "chronobio[dev]"
```

---

## Lancement du jeu

Vous pouvez lancer le jeu de deux manières :  

1. **En utilisant le fichier `launcher.py`**.  
```powershell
python launcher.py
```
2. **Ou en exécutant directement les commandes suivantes** dans l'environnement virtuel précédemment créé :
```powershell
python.exe -m chronobio.game.server -p 12345
python.exe -m chronobio.viewer -p 12345
python.exe -m main
```

---

## Stratégie
La stratégie mise en place repose sur une organisation précise des champs afin de séparer deux objectifs : générer rapidement de l’argent et alimenter la production de soupe.

Les deux premiers champs sont utilisés en boucle pour planter, récolter puis vendre directement les cultures. Cette boucle permet d’assurer une rentrée d’argent constante et rapide, nécessaire au fonctionnement et au développement de la ferme.

Les trois champs suivants ont un rôle différent. Ils ne servent pas à la vente directe, mais à produire des ressources destinées au stock de la fabrique. Ces ressources sont utilisées pour alimenter la soup factory, permettant une production continue de soupe, qui apporte une valeur plus importante à moyen terme.

Cette stratégie repose donc sur deux idées principales : garantir une stabilité économique immédiate grâce aux ventes directes, et mettre en place une chaîne de production autonome pour la soupe. Cette organisation permet de simplifier la logique du programme tout en rendant la gestion de la ferme plus efficace.

---

## Tests
### Installation
```powershell
python -m pip install pytest pytest-cov
```
### Lancer les tests avec couverture
```powershell
pytest --cov=src --cov-report=term-missing
```

---

## Structure du projet
```
Projet-POO-M1/
├── .github
├── src/
│   ├── farm/
│   │   ├── __init__.py
│   │   ├── employees.py
│   │   ├── field.py
│   │   ├── soup_factory.py
│   │   ├── stock_factory.py
│   │   └── tractors.py
│   └── strategie/
│   │   ├── __init__.py
│   │   ├── farm_strategy.py
│   │   └── base.py
├── tests/
│   ├── __init__.py
│   ├── test_employees.py
│   ├── test_field.py
│   ├── test_soup_factory.py
│   ├── test_stock_factory.py
│   └── test_tractors.py
├── .coveragerc
├── .gitignore
├── coverage.svg
├── launcher.py
├── main.py
└── README.md
```

---

## Contributeurs

- Guillaume LANDFROID-NAZAC 
- Mathis DÉRONNE
- Damien ZORZETTO
- Leo TISSOT
- Edwin LE ROYER

---

## Règles et sources

- Dépôt officiel du jeu Chronobio : https://github.com/vpoulailleau/chronobio
