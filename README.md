# HMP-Formation_DevSecOps

L'objectif de ce repository et de pouvoir fournir une formation DevSecOps la plus complète possible. Pour cela on exploite la CVE-2020-1747 qui permet à un utilisateur d'exécuter du code en injectant un fichier YAML.
L'application permet à un utilisateur de selectionner un fichier YAML et de l'upload. Il intègre, par défaut, la version 5.3 de la bibliothèque PyYAML qui est vulnérable à la CVE-2020-1747

Pré-requis :
- Avoir Git installé sur son PC
- Avoir un pc Windows
- Avoir un compte github

Etapes à suivre :

1) Télécharger le zip via github et le dézipper

2) Ouvrir le fichier requirements.txt et vérifier que la version de PyYAML est bien la 5.3 "PyYAML==5.3"

3) Avec python, lancer "application.py"

4) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Vous devriez tomber sur un application simple qui vous demande d'upload un fichier

5) Selectionner et upload le fichier "payload.yaml" et regarder votre terminal. La commande "dir" s'est exécutée et vous pouvoir la liste des fichiers et dossiers de votre repertoire. Cela veut donc dire la vulnérabilité a bien été exploitée.

6) Avec CTRL+C arréter l'exécution de l'application dans votre terminal. Taper la commande "pip install pyyaml==5.3.1". La vulnérabilité que l'on vient d'exploiter a été corrigée dans la version PyYAML 5.3.1.

7) Relancer l'application et vérifier quand le fichier "requirements.txt" s'est bien mis à jour et que la version de PyYAML est bien la 5.3.1 "PyYAML==5.3.1"

8) Aller sur le navigateur et dans la barre de navigation taper "127.0.0.1:5000". Essayer à nouveau d'envoyer le fichier YAML et regarder le terminal. Une erreur (500) devrait apparaître. Il n'est donc plus possible d'exploiter la vulnérabilité.

