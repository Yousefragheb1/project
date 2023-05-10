from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route ("/footy")
def footy():
    conn= sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Lesson")
    results = cur.fetchall()
    return render_template(""football.html" , results=results , title = FOOTBALL PAGE ")

@app.route('/footy/<int:id>')
def footy(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM lesson WHERE id=?',(id,))
    lesson = cur.fetchone()
    cur.execute('SELECT name FROM course WHERE id=?',(id,))
    course = cur.fetchone()
    return render_template('footy.html' , lesson=lesson , course=course)

if __name__ == "__main__":
 app.run(debug=True)