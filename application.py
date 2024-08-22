# pyyaml==5.3 required. Vulnerability has been fixed in 5.3.1
# pip install PyYAML==5.3
# CVE-2020-1747 
# More: ret2libc's report in https://github.com/yaml/pyyaml/pull/386
import yaml
import subprocess
import os
import pipreqs
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from pathlib import Path
import sys
from colorama import Fore, Back, Style, init
   

init() #Init colorama 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        file_name = file.filename
        file_content = process_file(file_name)
        print("file uploded !")
    return render_template('index.html', file_content=file_content)


def process_file(file_name):
    """Lit le fichier texte et retourne son contenu. Pour d'autres types de fichiers, ajustez le traitement."""
    print(file_name)
    if ".yaml" in file_name:
        with open(file_name,'rb') as f:
            content = f.read()
        data = yaml.load(content, Loader=yaml.FullLoader) # Using vulnerable FullLoader

        return data
    else:
        return "Uploaded file is not a YAML file."
    
def gen_reqtxt(directory):

    #Exécute pipreqs pour récupérer le nom des libs à mettre dans le requirements.txt
    subprocess.run([sys.executable, "-m", "pipreqs.pipreqs", "--force", directory])
    with open("installed_versions.txt", "w") as f:
        try:
            subprocess.run(["pip", "freeze"], stdout=f)
        except Exception as e:
            print(f'Erreur dans le fichier de freeze')

    #Récupère toutes les dépendances installées avec leur version
    all_lib_install = []
    with open("installed_versions.txt", "r") as file_install:
        for ligne in file_install:
            all_lib_install.append(ligne)
    os.remove("installed_versions.txt")

    #Récupère seulement le pattern (sans les versions) des dépendances à ajouter dans requirements.txt (ex: PyYAML==)
    lib_pipreqs = []
    with open("requirements.txt", "r") as file_pipreqs:
        for ligne in file_pipreqs:
            lib_pipreqs.append(ligne[:ligne.index('==')+2])

    #Fait le match pour récupérer les versions des dépendances présentes dans pipreqs
    final_lib = []
    for value in all_lib_install:
        if value[:value.index('==')+2] in lib_pipreqs:
            final_lib.append(value)

    #Ecrit le réquirements.txt
    with open("requirements.txt", "w") as f:
        for item in final_lib:
            f.write(item)



if __name__ == '__main__':
    directory = f'{Path(__file__).parent}'
    gen_reqtxt(directory)
    app.run(debug=False)
    """
    try:
        with open("installed_versions.txt", "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f)
        subprocess.run([sys.executable, "-m", "pipreqs.pipreqs", directory, "--use-local"])
        print(f'Fichier requirements.txt generé avec succès ! ')
    except Exception as e:
        print(f'Erreur dans la génération du requirements.txt : {e}')
   
"""
