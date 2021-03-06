from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html", articles = Articles)

@app.route("/article/<string:id>/")
def article(id):
    return render_template("article.html", id=id)

# debug = True paramter should be removed once app is complete
# this is only included so that server restarts are not required after every change
if __name__ == "__main__":
    app.run(debug = True)
