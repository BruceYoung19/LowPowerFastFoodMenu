from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("homepage.html")

@app.route("/user")
def newUser():
    return render_template("newuser.html")

if __name__ == '__main__':
    app.run()

