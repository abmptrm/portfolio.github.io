from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def about():
    return render_template('index.html')

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/email")
def email():
    return render_template("email.html")

@app.route("/phone")
def phone():
    return render_template("phone.html")

if __name__ == "__main__":
    app.run(debug=True)