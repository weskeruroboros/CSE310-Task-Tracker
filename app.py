from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy extension
db = SQLAlchemy(app)

# Define the Task relational database model
class Task(db.Model):
    """Database model representing individual tasks in the system."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')
    status = db.Column(db.String(20), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"

# Automatically create database tables within application context
with app.app_context():
    db.create_all()

# PAGE 1: View Tasks & Retrieve Data
@app.route('/')
def home():
    """Home route retrieving all task records from the relational database."""
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# PAGE 2: Add Task Page (Insert Data)
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Route handling GET to display input form and POST to insert a new task into the database."""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', 'General').strip()
        
        if title:
            new_task = Task(title=title, category=category, status='Pending')
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('home'))
            
    return render_template('add_task.html')

# Action Route: Toggle Task Status (Modify Data - Status)
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Action route updating/modifying a specific task's completion status in the database."""
    task = Task.query.get_or_404(task_id)
    task.status = 'Completed' if task.status == 'Pending' else 'Pending'
    db.session.commit()
    return redirect(url_for('home'))

# Action Route: Edit Task Details (Modify Data - Text/Category)
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Route handling GET to display edit form and POST to update task title and category."""
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        new_title = request.form.get('title', '').strip()
        new_category = request.form.get('category', 'General').strip()
        
        if new_title:
            task.title = new_title
            task.category = new_category
            db.session.commit()
            return redirect(url_for('home'))
            
    return render_template('edit_task.html', task=task)

# Action Route: Delete Task (Delete Data)
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Action route removing/deleting a task record from the database."""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

# PAGE 3: Third Dynamically Generated Page (Statistics using SQL Aggregate Functions)
@app.route('/stats')
def stats():
    """Third dynamic route using SQL aggregate functions (COUNT) to summarize database metrics."""
    total = db.session.query(db.func.count(Task.id)).scalar()
    completed = db.session.query(db.func.count(Task.id)).filter(Task.status == 'Completed').scalar()
    pending = (total if total is not None else 0) - (completed if completed is not None else 0)
    return render_template('stats.html', total=total, completed=completed, pending=pending)

if __name__ == '__main__':
    app.run(debug=True)