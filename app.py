from flask import Flask,render_template,url_for,redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Login management
#app.config[''] = ''
    #login_manager = LoginManager()
    #login_manager.init_app(app)
    #login_manager.login_view = 'login'

# PAGE REDIRECTION
@app.route("/")
def index():
     return render_template("homepage.html")

@app.route("/user")
def newuser():
    return render_template("newuser.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("aboutus.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

if __name__ == '__main__':
    app.run(debug = True)

