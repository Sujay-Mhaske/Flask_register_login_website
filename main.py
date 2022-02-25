import mysql.connector
from flask import *
import os

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sujya999$',
    port='3306',
    database='sujay_database',
    autocommit=True,
)
mycursor = mydb.cursor()
app.secret_key = os.urandom(24)


@app.before_request
def before_request():
    g.user = None
    if 'pass' in session:
        g.user = session['pass']


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print('user entered username', request.form['username'])
        print('user entered password', request.form['password'])
        mycursor.execute("SELECT Passwrd FROM sujay_database.persons WHERE Username='{}';".format(request.form['username']))
        pwd = mycursor.fetchall()
        print('database password', pwd)
        if pwd[0][0] == request.form['password']:
            return render_template('success.html', username=request.form['username'])
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        print('user entered username', request.form['username'])
        print('user entered password', request.form['password'])
        mycursor.execute("INSERT INTO Persons (Username, Passwrd) VALUES ('{}','{}');".format(request.form['username'], request.form['password']))
        return render_template('registered.html')

if __name__ == "__main__":
    app.run()
