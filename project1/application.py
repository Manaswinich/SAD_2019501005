# from flask import Flask, render_template, request, session
# from flask_session import Session
import os
from datetime import datetime
from flask import Flask, session, render_template, request, url_for, redirect
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


@app.route("/")
def homes():
    # return render_template("home.html")
    if session.get("data") is not None:
        return render_template("main.html")
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def reg():
    session["lis"] = []
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        gender = request.form.get("gender")
        birthday = request.form.get("birthday")
        email = request.form.get("email")

        usr = request.form.get("usr")
        password = request.form.get("psw")
        user = User(usr=usr, password=password, time=datetime.now())
        db.add(user)
        db.commit()
        return render_template("done.html", fname=fname, lname=lname, gender=gender, birthday=birthday, email=email)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        if session.get("data") is not None:
            return render_template("main.html")
        return render_template("login.html")
    elif request.method == "POST":
        usr = request.form.get("usr")
        psw = request.form.get("psw")
        user = db.query(User).get(usr)
        # f = open("test.txt", "w+")
        # f.write(user)
        # print(user.usr)
        if user is not None:
            if usr == user.usr and psw == user.password:
                session["data"] = usr
                return render_template("main.html")
        return redirect(url_for("reg"))


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for('login'))
    # return render_template("logout.html")


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
