from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# Define a route for the home page


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/passing')
def passing():
    return render_template('passing.html')


@app.route('/shooting')
def shooting():
    return render_template('shooting.html')


@app.route('/dribbling')
def dribbling():
    return render_template('dribbling.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")

# Establish a connection to the SQLite database named "database.db"
# Create a cursor to interact with the database
# Execute an SQL query to select all records from the "course" table
# Fetch all the results (rows) from the executed query
# Render an HTML template named "course.html" and pass the results


@app.route("/course")
def course():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM course ")
    results = cur.fetchall()
    return render_template("course.html", results=results, title="course")

# does same as code over it
@app.route('/football/<int:id>')
def football(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM course WHERE id=?', (id,))
    football = cur.fetchone()
    print(football)
    return render_template('football.html', football=football)

# Define a custom error handler for 404 errors  


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# Run the Flask application


if __name__ == "__main__":
    app.run(debug=True) 