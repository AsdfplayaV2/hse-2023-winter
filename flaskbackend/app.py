# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Your routes and models go here
@app.route('/')
def hello():
    return 'Hello, Flask in Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


