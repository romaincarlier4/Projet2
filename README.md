# Projet2 - ReadMe
 ![version](https://img.shields.io/badge/version-2.1.0-purple.svg) 
Rédigé par Ralph Abona

## Structure de fichiers
Après téléchargement, vous trouverez les répertoires et fichiers suivants:
```
Projet2-Master/
├── README.md
├── LICENSE.md
└── FlaskApp
    └── App
        ├── inginious.sqlite
        ├── app.py
        ├── db.py
        ├── __pychache__/
        ├── scripts/
        ├── static
        │   ├── inginious.sqlite
        │   ├── assets
        │   │   ├── css
        │   │   │   ├── style.css
        │   │   │   ├── black-dashboard.css
        │   │   │   ├── black-dashboad.css.map
        │   │   │   ├── black-dashboard.min.css
        │   │   │   └── nucleo-icons.css
        │   │   ├── scss
        │   │   │   ├── black-dashboard.scss
        │   │   │   └── black-dashboard
        │   │   │       └── ...
        │   │   ├── js
        │   │   │   ├── main.js
        │   │   │   ├── black-dashdoard.js
        │   │   │   ├── black-dashboard.js.map
        │   │   │   ├── black-dashboard.min.js
        │   │   │   ├── core
        │   │   │   └── plugins
        │   │   ├── img
        │   │   │   ├── apple-touch-icon.png
        │   │   │   ├── cta-bg.jpg
        │   │   │   ├── favicon.png
        │   │   │   ├── hero-bg.pg
        │   │   │   ├── logo.png
        │   │   │   ├── clients
        │   │   │   │   ├── client-1.png
        │   │   │   │   ├── client-2.png
        │   │   │   │   ├── client-3.png
        │   │   │   │   └── client-4.png
        │   │   │   └── teamm
        │   │   │       ├── team-1.png
        │   │   │       ├── team-2.png
        │   │   │       ├── team-3.png
        │   │   │       └── team-4.png
        │   │   ├── demo
        │   │   │   ├── demo.css
        │   │   │   └── demo.js
        │   │   ├── fonts
        │   │   │   ├── nucleo.eot
        │   │   │   ├── nucleo.ttf
        │   │   │   ├── nucleo.woff
        │   │   │   └── nucleo.woff2
        │   │   └── vendor
        │   │       └── ...
        ├── templates
        │   ├── app.html
        │   ├── credits.html
        │   ├── doc.html
        │   ├── index.html
        │   ├── LEPL1402
        │   ├── LSIF1101_PYTHON.html
        │   ├── LSINF1252.html
        │   ├── projet.html
        │   ├── stat.html
        │   └── static
        │       └── ...
        └── venv
            ├── pyvenv.cfg
            ├── bin
            │   ├── ...
            └── lib
                └── ...
```

## Navigateurs supportés

Le projet fonctionne de manière optimale avec les navigateur suivants :

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64">  <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64">

De légers bugs d'affichage peuvent être constatés avec chrome.

## Comment utiliser l'application

Etapes pour lancer le site:

1) Ouvrir l'invite de commande et se rendre dans le fichier "..\Projet2", c'est à dire le fichier parent de Groupe10

2) Lancer la commande "Projet2\Scripts\activate" pour activer l'environnement virtuel

3) Rendez vous dans le fichier App grâce à la commande "cd Projet2\FlaskApp\App"

4) Lancer la commande "flask run"

5) Ouvrez votre navigateur et taper dans la barre de recherche "http://127.0.0.1:5000"

6) Pour fermer votre environement virtuel, rentrer la la commande "deactivate"

## Problèmes courants

### Problèmes d'affichage
Des bugs d'affichages peuvent être observés si 
- Un navigateur non supporté ou non mis-à-jour est utilisé
- Si le site est affiché sur un écran ayant un ration non standard 

## Licensing

- Copyright Avril 2020 Ralph Abona, Igor Bertrand & Romain Carlier
- Sous licence MIT (https://github.com/byralph/Projet2/LICENSE.md)

