# ProductiviTime

ProductiviTime is a Flask-based productivity web application created as my CS50 final project. It helps users organize tasks, schedule events, and track countdowns for important dates through one simple dashboard.

Demo video: https://www.youtube.com/watch?v=9otSehOOepg

## Project Overview

ProductiviTime gives users three main productivity modules:

- **Calendar**: add events by date and display them in a calendar interface.
- **Countdowns**: automatically show how much time is left until saved events.
- **To-Do List**: add tasks, edit tasks, delete tasks, and update task status.

The app includes user registration, login, session-based authentication, and a SQLite database that stores users, events, and tasks separately for each account.

## Features

- User registration
- User login and logout
- Session-based route protection
- Homepage dashboard
- Calendar event creation
- Event storage by user
- Countdown display for saved events
- Event deletion from countdowns
- To-do task creation
- To-do task editing
- To-do task deletion
- Task status cycling: Todo, In Progress, Complete
- SQLite database integration
- AJAX-based task updates
- FullCalendar integration
- Bootstrap-based interface

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

## Repository Structure

```text
productivitime/
├── application.py
├── helpers.py
├── project.db
├── requirements.txt
├── README.md
├── database/
│   └── schema.sql
├── licenses/
│   ├── FULLCALENDAR LICENSE.txt
│   └── TODOLIST LICENSE.txt
├── static/
│   ├── styles.css
│   └── README.md
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
git clone https://github.com/YOUR-USERNAME/productivitime.git
cd productivitime
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set the Flask app

On Windows PowerShell:

```powershell
$env:FLASK_APP = "application.py"
```

On macOS or Linux:

```bash
export FLASK_APP=application.py
```

### 5. Run the application

```bash
flask run
```

Then open the local link shown in the terminal.

## Database

This repository includes a clean `project.db` database generated from the original schema. The schema is also included in:

```text
database/schema.sql
```

The database stores:

- Users and password hashes
- Calendar events
- To-do tasks
- Task status values

## Notes

This project was originally built in the CS50 IDE as a CS50 final project. The uploaded version has been organized into a standard Flask project structure for GitHub.

The original homepage references image files named `calendar.png`, `todolist.png`, and `countdown.png`. Add those files into the `static/` folder if you recover them.

## Credits and Licenses

This project uses FullCalendar and a to-do list UI reference. Their license files are included in the `licenses/` folder.

## Future Improvements

Possible future updates include:

- Modernizing the UI
- Adding responsive layouts
- Improving date validation
- Adding event editing
- Adding countdown sorting
- Adding screenshots to this README
- Deploying the app online
