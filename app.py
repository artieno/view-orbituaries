from flask import Flask, request, render_template
import sqlite3
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('obituary_form.html')

@app.route('/submit_obituary', methods=['POST'])
def submit_obituary():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    date_of_death = request.form['date_of_death']
    content = request.form['content']
    author = request.form['author']
    slug = hashlib.md5(name.encode()).hexdigest()

    conn = sqlite3.connect('obituary_platform.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author, slug)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, date_of_birth, date_of_death, content, author, slug))

    conn.commit()
    conn.close()
    
    return "Obituary submitted successfully! <a href='/view_obituaries'>View all obituaries</a>"

@app.route('/view_obituaries')
def view_obituaries():
    conn = sqlite3.connect('obituary_platform.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM obituaries')
    obituaries = cursor.fetchall()
    conn.close()

    return render_template('view_obituaries.html', obituaries=obituaries)

if __name__ == '__main__':
    app.run(debug=True)
