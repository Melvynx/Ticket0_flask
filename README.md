# TiQeto Epsic with Python - Flask

> Installer un repo github avec ses dépendance

*Module 104 - Epsic*

Tuto pour que n'importe quelle personne puisse installer mon projet.


## Git - cloner le repository

Pour cloner le repository, il vous suiffira d'ouvrir un terminal.

Si vous n'avez pas git, il faudra [le télécharger ici](https://git-scm.com/).

Ensuite rentrer dans le dosier dans lequelle vous souhaiter que le projet s'install.
```bash
mac@/$ cd dev/python
```
Puis y cloner le projet avec la commande `git clone <liens>`
```bash
mac@/Dev/Python/$ git clone https://github.com/MelvynX/Tiqeto_Epsic.OM.git

Cloning into 'Tiqeto_Epsic.OM'...
remote: Enumerating objects: 248, done.
remote: Counting objects: 100% (248/248), done.
remote: Compressing objects: 100% (130/130), done.
remote: Total 248 (delta 102), reused 223 (delta 82), pack-reused 0
Receiving objects: 100% (248/248), 47.08 KiB | 573.00 KiB/s, done.
Resolving deltas: 100% (102/102), done.
```

Voilà 🤩 vous êtes en possession du projet sur votre machine !


## Installer les dépendences Python

Pour ceci, il vous suffira dans l'éditeur `PyCharm` d'aller dans le section `settings`.

Ici, vous allez séléctionner le réglage `Projet: Nom_Du_Projet`.

Aller en haut à droite sur le `+` cliquer sur `add`.

![](https://i.imgur.com/H6xm15r.png)

Ici, vous n'avez plus qu'à choisir le dossier `venv` et télécharger les dépendences.

## Installer les dépendences package.json
*Pour le javascript et css.*

Ici, il faudra ouvrir un terminal.

Rentrer dans le projet.
```bash
mac@/$ cd dev/python/Tiqeto
```
Il faudra rentrer dans le dossier `app` puis dans `static`.
```bash
mac@/dev/python/Tiqeto$ cd app/static
```
Ici, si vous ne possédé pas `npm` ou `yarn` il vous faudra l'installer.

[🐳yarn](https://yarnpkg.com/) / [🦀npm](https://www.npmjs.com/)

Puis tout simplement faire
```bash
# with yarn
mac@/dev/python/Tiqeto/app/static$ yarn init

#with npm
mac@/dev/python/Tiqeto/app/static$ npm i
```

Et voilà, vous pouvez maintenant lancer l'application sur le fichier `run.py` en utilisant **pycharm**.

*Melvyn Malherbe*

> [time=Thu, Apr 9, 2020 10:33 PM]
