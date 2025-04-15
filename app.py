from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("homepage.html")

@app.route("/user")
def newuser():
    return render_template("newuser.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()

