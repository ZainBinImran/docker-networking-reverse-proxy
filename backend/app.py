import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "postgres-container"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "network_lab"),
    "user": os.getenv("DB_USER", "netapp"),
    "password": os.getenv("DB_PASSWORD"),
}


@app.route("/")
def index():
    return jsonify({
        "service": "backend",
        "status": "running"
    })


@app.route("/api/health")
def health():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_database(), current_user")
                database, user = cur.fetchone()

        return jsonify({
            "service": "backend",
            "status": "healthy",
            "database": database,
            "database_user": user
        })

    except Exception as e:
        return jsonify({
            "service": "backend",
            "status": "unhealthy",
            "error": str(e)
        }), 500


app.run(host="0.0.0.0", port=5000)
