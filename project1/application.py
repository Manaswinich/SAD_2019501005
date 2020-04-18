# from flask import Flask, render_template, request, session
# from flask_session import Session
import os
from datetime import datetime
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
database = scoped_session(sessionmaker(bind=engine))
db = database()

lis = []
# data = []


@app.route("/", methods=["GET", "POST"])
def home():
    # if request.method == "GET":
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def reg():
    # if session.get("lis") is None:
    session["lis"] = []
    # session["data"] = []
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        fname = request.form.get("fname")
        # session["lis"].append(fname)
        lname = request.form.get("lname")
        # session["lis"].append(lname)
        gender = request.form.get("gender")
        # session["lis"].append(gender)
        birthday = request.form.get("birthday")
        # session["lis"].append(birthday)
        email = request.form.get("email")
        # session["lis"].append(email)
        usr = request.form.get("usr")
        session["lis"].append(usr)
        password = request.form.get("psw")
        session["lis"].append(password)
        user = User(usr=usr, password=password, time=datetime.now())
        db.add(user)
        db.commit()
        return render_template("done.html", fname=fname, lname=lname, gender=gender, birthday=birthday, email=email)


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    return render_template("logout.html")


@app.route("/admin")
def admin():
    us = db.query(User).order_by(desc(User.time))
    # us = User.query.order_by("time").all()
    return render_template("admin.html", us=us)


@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)
