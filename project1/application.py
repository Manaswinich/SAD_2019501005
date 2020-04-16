# from flask import Flask, render_template, request, session
# from flask_session import Session
import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
# raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


lis = []


@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def reg():
    # if session.get("lis") is None:
    session["lis"] = []
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        lis = request.form.get("fname")
        session["lis"].append(lis)
        return render_template("done.html", fname=session["lis"][0])


if __name__ == '__main__':
    app.run(debug=True)
