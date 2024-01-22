from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# PostgreSQL configuration
db_config = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'postgres',  # This is the name of the PostgreSQL service in Docker Compose
    'port': '5432',
}

def create_connection():
    return psycopg2.connect(**db_config)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    with create_connection() as connection, connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM tasklist")
        tasks = cursor.fetchall()
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    with create_connection() as connection, connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM tasklist WHERE id = %s", (task_id,))
        task = cursor.fetchone()
    if task is not None:
        return jsonify(task)
    else:
        return jsonify(message="Task not found"), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    with create_connection() as connection, connection.cursor() as cursor:
        cursor.execute("INSERT INTO tasklist (taskname, completed) VALUES (%s, %s) RETURNING *",
                       (data['taskname'], data['completed']))
        new_task = cursor.fetchone()
        connection.commit()
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
