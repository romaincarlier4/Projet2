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

De légers bugs d'affichage peuvent être constatés avec Safari.

## Comment utiliser l'application

### Lancer l'application :

#### Sur Windows

1) Créé un environnement virtuel, pour cela, rendez vous dans le dossier parent au dossier de notre projet ( ..\Projet2) puis lancer ceci, « python3 -m venv Projet2». Normalement, votre environnement est crée.

2) Ensuite, activer votre environnement comme ceci : « Projet2\Scripts\activate ».

3) Téléchargez flask : rendez vous dans le dossier Projet2 et lancer la commande « pip install flask »

4) Une fois flask installé, rendez vous dans le dossier App (« Projet2\FlaskApp\App ») et lancer la commande « flask run » depuis ce dossier.

5) Pour finir, rendez vous dans votre navigateur et taper l’url qui vous est donnée dans l’invite de commande ("http://127.0.0.1:5000/").


#### Sur MacOS/Linux

1) Créé un environnement virtuel, pour cela, rendez vous dans le dossier parent au dossier de notre projet ( ..\Projet2) puis lancer ceci, « python3 -m venv Projet2». Normalement, votre environnement est crée.

2) Ensuite, activer votre environnement comme ceci : « source Projet2/bin/activate ».

3) Téléchargez flask : rendez vous dans le dossier Projet2 et lancer la commande « pip install flask »

4) Une fois flask installé, rendez vous dans le dossier App (« Projet2\FlaskApp\App ») et lancer la commande « flask run » depuis ce dossier.

5) Pour finir, rendez vous dans votre navigateur et taper l’url qui vous est donnée dans l’invite de commande ("http://127.0.0.1:5000/").

## Problèmes courants

### Problèmes d'affichage
Des bugs d'affichages peuvent être observés si 
- Un navigateur non supporté ou non mis-à-jour est utilisé
- Si le site est affiché sur un écran ayant un ratio non standard

## Licensing

- Avril 2020 Ralph Abona, Igor Bertrand & Romain Carlier
- Licence (https://github.com/byralph/Projet2/LICENSE.md)

