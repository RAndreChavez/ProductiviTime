import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    if request.method == "GET":

        return render_template("index.html")

    else:
        return redirect('/')


@app.route("/calendar", methods=["GET", "POST"])
@login_required
def calendar():
    """Opens Calendar"""

    user_id = session["user_id"]

    events = [
    {
        'name' : 'test',
        'date' : '2001-07-09',
    },
]

    if len(db.execute("SELECT title FROM events WHERE user_id = ?", user_id)) >= 1:

        keys = range(len(db.execute("SELECT title FROM events WHERE user_id = ?", user_id)))

        for i in keys:
            name = db.execute("SELECT title FROM events WHERE user_id = ?", user_id)[i]["title"]
            date = db.execute("SELECT start FROM events WHERE user_id = ?", user_id)[i]["start"]

            if len(events) <= len(db.execute("SELECT title FROM events WHERE user_id = ?", user_id)):
                    events.append({
                    'name' : name,
                    'date' : date,
                },
                )

    if request.method == "POST":
        day = request.form.get("days")
        month = request.form.get("months")
        year = request.form.get("years")
        event = request.form.get("event")
        completedate = year + "-" + month + "-" + day

        if not event:
            return apology("Event name needed")

        elif month == "02" and int(day) > 28:
            return apology("Invalid date")

        elif month == "04" and int(day) > 30:
            return apology("Invalid date")

        elif month == "06" and int(day) > 30:
            return apology("Invalid date")

        elif month == "09" and int(day) > 30:
            return apology("Invalid date")

        elif month == "11" and int(day) > 30:
            return apology("Invalid date")

        else:
            events.append({
                'name' : event,
                'date' : completedate,
            },
            )
            db.execute("INSERT INTO events (user_id, title, start) VALUES (?, ?, ?)",
                       user_id, event, completedate)

        return redirect('/calendar')
    else:
        return render_template("calendar.html", events = events)

@app.route("/countdowns", methods=["GET", "POST"])
@login_required
def countdowns():
    """Opens Countdowns"""

    user_id = session["user_id"]

    if request.method == "POST":
        toDelete = request.form.get("delete")
        db.execute("DELETE FROM events WHERE title = ?", toDelete)
        return redirect('/countdowns')

    else:
        events = db.execute("SELECT start, title FROM events WHERE user_id = ?", user_id)
        return render_template("countdowns.html", events = events)

@app.route("/todolists", methods=["GET", "POST"])
@login_required
def todolists():
    """Opens TO-DO Lists"""

    items = fetch_todo()

    return render_template("todolists.html", items = items)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}

    return jsonify(result)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("confirmation"):
            return apology("must confirm password")

        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("Password must match")

        hash = generate_password_hash(request.form.get("password"))

        # Query database for username
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), hash)
            return redirect("/")
        except:
            return apology('Username is already in use', 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

def fetch_todo() -> dict:
    user_id = session["user_id"]

    todo_list = []

    if len(db.execute("SELECT task FROM tasks WHERE user_id = ?", user_id)) >= 1:

        keys = range(len(db.execute("SELECT task FROM tasks WHERE user_id = ?", user_id)))

        for i in keys:
            task_id = db.execute("SELECT id FROM tasks WHERE user_id = ?", user_id)[i]["id"]
            task = db.execute("SELECT task FROM tasks WHERE user_id = ?", user_id)[i]["task"]
            status = db.execute("SELECT status FROM tasks WHERE user_id = ?", user_id)[i]["status"]

            item = {
                "id": task_id,
                "user_id": user_id,
                "task": task,
                "status": status,
            }
            todo_list.append(item)

    return todo_list

def update_task_entry(task_id: int, text: str) -> None:
    user_id = session["user_id"]
    db.execute("UPDATE tasks SET task = ? WHERE id = ? AND user_id = ?", text, task_id, user_id)

def update_status_entry(task_id: int, text: str) -> None:
    user_id = session["user_id"]
    db.execute("UPDATE tasks SET status = ? WHERE id = ? AND user_id = ?", text, task_id, user_id)

def insert_new_task(text: str) ->  int:
    user_id = session["user_id"]
    stat = "Todo"
    db.execute("INSERT INTO tasks (user_id, task, status) VALUES (?, ?, ?)", user_id, text, stat)
    task_id = db.execute("SELECT id FROM tasks WHERE user_id = ?", user_id)

    return task_id

def remove_task_by_id(task_id: int) -> None:
    user_id = session["user_id"]
    db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", task_id, user_id)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
