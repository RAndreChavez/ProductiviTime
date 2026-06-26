# ProductiviTime

ProductiviTime is a Flask-based productivity web application created as my CS50 final project. It was my first complete personal web application and was designed to help users organize their time, events, and tasks in one place.

Video demo: https://www.youtube.com/watch?v=9otSehOOepg

## Description

ProductiviTime helps users stay organized through three main productivity tools:

- A calendar for saving events
- A countdowns page for tracking time left until saved events
- A to-do list for managing tasks and task status

The application includes user registration, login, logout, session-based authentication, database-backed event storage, and AJAX-based task updates.

## Main Features

### User Authentication

Users can register with a username, password, and password confirmation. After registering, users can log in and access their personal productivity dashboard.

### Homepage Dashboard

After logging in, users are taken to a homepage with three main modules:

- Calendar
- Countdowns
- To-Do List

### Calendar

The calendar module allows users to add events by selecting a day, month, year, and event title. Events are saved in the database and displayed on the calendar.

### Countdowns

The countdowns module displays how many days, hours, minutes, and seconds are left until each saved event. Events shown here are connected to the calendar database. Users can also delete events from the countdowns page.

### To-Do List

The to-do list module allows users to:

- Add tasks
- Edit task descriptions
- Delete tasks
- Update task status

Tasks can move between these statuses:

- Todo
- In Progress
- Complete

## Technologies Used

- Python
- Flask
- Flask-Session
- CS50 SQL Library
- SQLite
- HTML
- CSS
- JavaScript
- AJAX
- Bootstrap
- FullCalendar

## Project Structure

```text
productivitime/
├── application.py
├── helpers.py
├── project.db
├── requirements.txt
├── README.md
├── FULLCALENDAR LICENSE.txt
├── TODOLIST LICENSE.txt
├── static/
│   └── styles.css
└── templates/
    ├── apology.html
    ├── calendar.html
    ├── countdowns.html
    ├── index.html
    ├── layout.html
    ├── login.html
    ├── register.html
    └── todolists.html
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/RAndreChavez/productivitime.git
cd productivitime
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -m venv .venv
```

On macOS or Linux:

```bash
python3 -m venv .venv
```

### 3. Install dependencies

You can install the dependencies without activating the virtual environment.

On Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On macOS or Linux:

```bash
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
```

### 4. Run the application

On Windows PowerShell:

```powershell
$env:FLASK_APP = "application.py"
.\.venv\Scripts\python.exe -m flask run
```

On macOS or Linux:

```bash
export FLASK_APP=application.py
./.venv/bin/python -m flask run
```

Then open the local URL shown in the terminal.

## Database

The application uses SQLite through the CS50 SQL Library.

The database file is:

```text
project.db
```

The application connects to it in `application.py` with:

```python
db = SQL("sqlite:///project.db")
```

Because of this, `project.db` should stay in the same folder as `application.py`.

## Credits and Licenses

This project uses FullCalendar and a to-do list interface reference. The original license files are included in this repository:

- `FULLCALENDAR LICENSE.txt`
- `TODOLIST LICENSE.txt`

