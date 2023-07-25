from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

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


@app.route("/course")
def course():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM course ")
    results = cur.fetchall()
    return render_template("course.html", results=results, title="course")

@app.route('/football/<int:id>')
def football(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM course WHERE id=?', (id,))
    football = cur.fetchone()
    print(football)
    cur.execute('SELECT name FROM course WHERE id=?', (football[2],))
    review = cur.fetchone()
    return render_template('football.html', football=football, review=review)


if __name__ == "__main__":
    app.run(debug=True)