from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from pyresparser import ResumeParser
from flask_cors import CORS,cross_origin
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@cross_origin()
def home_page():
    return render_template("home_page.html")

@app.route("/about",methods=["GET","POST"])
@cross_origin()
def about_page():
    return render_template("about.html")

@app.route("/evaluate",methods=["GET","POST"])
@cross_origin()
def upload_resume():
    files=None
    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            file.save("./resumes/"+secure_filename(file.filename))
    return ResumeParser("./resumes/"+str(files[0].filename)).get_extracted_data()


if __name__=="__main__":
    app.run(debug=True)