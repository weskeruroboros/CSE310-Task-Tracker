from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def load_tasks():
    """Reads tasks from the JSON file persistence layer."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Saves updated tasks list back to JSON file storage."""
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# PAGE 1: View Tasks & Toggle Completion
@app.route('/')
def home():
    """Home route displaying all tasks loaded from persistent storage."""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

# PAGE 2: Add Task Page (Interactive User Input Form)
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Route handling GET to display form and POST to save new user input task."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', 'General').strip()
        if title:
            tasks = load_tasks()
            new_task = {
                'id': len(tasks) + 1,
                'title': title,
                'category': category,
                'status': 'Pending'
            }
            tasks.append(new_task)
            save_tasks(tasks)
            return redirect(url_for('home'))
    return render_template('add_task.html')

# Action Route: Toggle Task Status
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Action route modifying task completion status upon user interaction."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed' if task['status'] == 'Pending' else 'Pending'
            break
    save_tasks(tasks)
    return redirect(url_for('home'))

# PAGE 3: Third Dynamically Generated Page (Statistics Summary)
@app.route('/stats')
def stats():
    """Third dynamic route aggregating real-time data metrics for user tasks."""
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get('status') == 'Completed')
    pending = total - completed
    return render_template('stats.html', total=total, completed=completed, pending=pending)

if __name__ == '__main__':
    # Launches the local test server at http://127.0.0.1:5000/
    app.run(debug=True)