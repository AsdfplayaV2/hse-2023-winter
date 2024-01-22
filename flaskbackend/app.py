from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)
CORS(app)

# Configure OpenTelemetry
trace.set_tracer_provider(TracerProvider(resource=Resource.create({'service.name': 'your-flask-service'})))
tracer_provider = trace.get_tracer_provider()

# Configure a Jaeger exporter. Replace 'your-jaeger-collector' with the actual address.
jaeger_exporter = JaegerExporter(agent_host_name='your-jaeger-collector', agent_port=6831)

# Create a BatchSpanProcessor and add the exporter
span_processor = BatchSpanProcessor(jaeger_exporter)
tracer_provider.add_span_processor(span_processor)

# Instrument Flask
FlaskInstrumentor().instrument_app(app)

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

@app.route('/tasks/<int:task_id>', methods=['GET', 'POST', 'DELETE'])
def get_update_or_delete_task(task_id):
    if request.method == 'GET':
        with create_connection() as connection, connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM tasklist WHERE id = %s", (task_id,))
            task = cursor.fetchone()
        if task is not None:
            return jsonify(task)
        else:
            return jsonify(message="Task not found"), 404
    elif request.method == 'POST':
        data = request.json
        with create_connection() as connection, connection.cursor() as cursor:
            cursor.execute("UPDATE tasklist SET completed = %s WHERE id = %s RETURNING *", (data['completed'], task_id))
            updated_task = cursor.fetchone()
            if updated_task is not None:
                connection.commit()
                return jsonify(updated_task)
            else:
                return jsonify(message="Task not found"), 404
    elif request.method == 'DELETE':
        with create_connection() as connection, connection.cursor() as cursor:
            cursor.execute("DELETE FROM tasklist WHERE id = %s RETURNING *", (task_id,))
            deleted_task = cursor.fetchone()
            if deleted_task is not None:
                connection.commit()
                return jsonify(deleted_task)
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
