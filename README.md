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

### Note 
Pour générer un `coverage.svg` :
```powershell
pip install pytest pytest-cov coverage
```
```powershell
pytest --cov=src --cov-report=xml
```
```powershell
coverage-badge -o coverage.svg
```
N'oubliez pas de faire un push si vous voulez voir les changements dans le README.

Autres commandes :
```
pytest --cov=src --cov-report=term-missing
```
```
pytest --cov --cov-branch
```

