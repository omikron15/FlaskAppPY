from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

# debug = True paramter should be removed once app is complete
# this is only included so that server restarts are not required after every change
if __name__ == "__main__":
    app.run(debug = True)
