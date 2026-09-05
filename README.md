# CSE 310 – Web Application Module: Task Tracker

## Overview
Task Tracker is a lightweight dynamic web application built using Python and Flask. It allows users to manage daily tasks, track completion statuses, and view real-time statistics regarding task progress.

## Web Application Features
* **Dynamic Web Pages:** Serves multiple HTML views using Jinja2 templating (`/`, `/add`, `/stats`).
* **User Interactivity:** Form handling allows users to dynamically create new tasks and toggle task completion.
* **Database & Storage:** Persists task data in a structured JSON file (`tasks.json`).
* **Local Test Server:** Runs locally via Flask's built-in WSGI development server.

## Development Environment
* **Language:** Python 3
* **Framework:** Flask
* **Frontend:** HTML5 / CSS3 (Jinja2 Templates)
* **Storage:** JSON File I/O

## Useful Websites
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Jinja Template Documentation](https://jinja.palletsprojects.com/)

## Future Work
* Integrate a full SQL database (PostgreSQL / SQLite).
* Add user authentication and login sessions.
* Implement task deadline alerts and priority sorting.