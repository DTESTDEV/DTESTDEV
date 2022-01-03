import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

from helpers import BELLprocess, BELLprocess2, ThinkTelprocess, ThinkTelprocess2, Tel_synergyprocess, Tel_synergyprocess2, voipmsprocess, voipmsprocess2

import csv



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pass1', methods=['GET', 'POST'])
def pass1():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            nofiles = 'No Files Selected'
            return render_template("pass1.html", message=nofiles)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if not file:
            #lash('No selected file')
            noseleted = 'No Files Selected'
            return render_template("pass1.html", message=noseleted)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = 'File Uploaded Successfully'
            return render_template("pass1.html", message=success)
            #return redirect(url_for('download_file', name=filename))

    else:
        return render_template("pass1.html")


@app.route('/pass2', methods=['GET', 'POST'])
def pass2():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            nofiles = 'No Files Selected'
            return render_template("pass2.html", message=nofiles)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if not file:
            #lash('No selected file')
            noseleted = 'No Files Selected'
            return render_template("pass2.html", message=noseleted)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = 'File Uploaded Successfully'
            return render_template("pass2.html", message=success)
            #return redirect(url_for('download_file', name=filename))

    else:
        return render_template("pass2.html")



@app.route("/process", methods=["GET", "POST"])
def process():
    providers_list = ["Bell", "ThinkTel", "Tel-synergy", "voip.ms"]
    if request.method == "POST":
        #yes = request.form.get("yes")
        #if yes == "yes":
        provider = request.form.get("provider")
        indexing = providers_list.index(provider)

        if indexing == 0:
            results = BELLprocess()
            return render_template("processed.html", results=results)
        elif indexing == 1:
            results = ThinkTelprocess()
            return render_template("processed.html", results=results)
        elif indexing == 2:
            results = Tel_synergyprocess()
            return render_template("processed.html", results=results)
        elif indexing == 3:
            results = voipmsprocess()
            return render_template("processed.html", results=results)
    else:
        return render_template("process.html", providers=providers_list)


@app.route("/process2", methods=["GET", "POST"])
def process2():
    providers_list = ["Bell", "ThinkTel", "Tel-synergy", "voip.ms"]
    if request.method == "POST":
        provider = request.form.get("provider")
        indexing = providers_list.index(provider)

        if indexing == 0:
            results = BELLprocess2()
            return render_template("processed2.html", results=results)
        elif indexing == 1:
            results = ThinkTelprocess2()
            return render_template("processed2.html", results=results)
        elif indexing == 2:
            results = Tel_synergyprocess2()
            return render_template("processed2.html", results=results)
        elif indexing == 3:
            results = voipmsprocess2()
            return render_template("processed2.html", results=results)

    else:
        return render_template("process2.html", providers=providers_list)


'''
@app.route("/process", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        #yes = request.form.get("yes")
        #if yes == "yes":
        results = DIDprocess()
        #print(type(results))
        return render_template("processed.html", results=results)
    else:
        return render_template("process.html")

'''



'''@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

'''








'''

import os
from flask import Flask, render_template, request

import csv

app = Flask(__name__)

wsgi_app = app.wsgi_app


@app.route('/', methods=["GET", "POST"])
def data():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join('uploads', file.filename))
        return render_template("index.html", message="success")
    else:
        return render_template("index.html", message="upload")


if __name__ == '__main__':
    app.run(debug=True)


'''