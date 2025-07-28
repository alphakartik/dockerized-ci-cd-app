from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'admin')
    db_pass = os.environ.get('DB_PASS', 'password')
    try:
        conn = psycopg2.connect(
            host=db_host, user=db_user, password=db_pass, dbname="postgres"
        )
        conn.close()
        return f"Hello from Flask! Connected to DB at {db_host}"
    except Exception as e:
        return f"DB connection error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
