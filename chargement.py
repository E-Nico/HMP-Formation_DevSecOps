# pyyaml==5.3 required. Vulnerability has been fixed in 5.3.1
# pip install PyYAML==5.3
# CVE-2020-1747
# More: ret2libc's report in https://github.com/yaml/pyyaml/pull/386
# Explanation: https://2130706433.net/blog/pyyaml/
import yaml
from flask import Flask, render_template, request, redirect, url_for
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename

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
    return render_template('index.html', file_content=file_content)

    #return render_template('index.html', file_name=file_name, file_content=file_content)

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
    


if __name__ == '__main__':
    app.run(debug=True)

