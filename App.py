from flask import Flask
from flask import render_template

app = Flask(__name__)


# @app.route("/")
# def main():
#     return render_template('index.html')

# @app.route("/s/<username>")
# def main(username):
#     return f"{render_template('index.html')} <script>alert('Halo {username}')</script>"

@app.route("/home")
def about():
    return render_template('index.html')

@app.route("/project")
def project():
    return render_template("project.html")

if __name__ == "__main__":
    app.run(debug=True)