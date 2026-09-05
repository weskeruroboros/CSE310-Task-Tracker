# CSE 310 – Web Application Module: Task Tracker

## Overview
Task Tracker is a lightweight dynamic web application built using Python and Flask. It allows users to manage daily tasks, track completion statuses, and view real-time statistics regarding task progress.

## Video Demonstration
* [Watch the Task Tracker Walkthrough Video](https://youtu.be/l1uTUSwpOLE)

## Web Application Features
* **Dynamic Web Pages:** Serves multiple HTML views using Jinja2 templating (`/`, `/add`, `/stats`).
* **User Interactivity:** Form handling allows users to dynamically create new tasks and toggle task completion.
* **Database & Storage:** Persists task data in a structured JSON file (`tasks.json`).
* **Local Test Server:** Runs locally via Flask's built-in WSGI development server.

## How to Run
1. Ensure Python 3 and Flask are installed on your system.
2. Open your terminal in the project root directory.
3. Start the application by running:
   ```bash
   python app.py