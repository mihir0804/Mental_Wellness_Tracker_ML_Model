import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data/logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT,
            predicted_emotion TEXT,
            confidence REAL,
            feedback TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(text, emotion, confidence):
    conn = sqlite3.connect("data/logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO emotions (input_text, predicted_emotion, confidence, timestamp)
        VALUES (?, ?, ?, ?)
    """, (text, emotion, confidence, datetime.now()))
    conn.commit()
    conn.close()

def update_feedback(entry_id, feedback):
    conn = sqlite3.connect("data/logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE emotions SET feedback = ? WHERE id = ?
    """, (feedback, entry_id))
    conn.commit()
    conn.close()

import sqlite3

# Connect to the database (will create logs.db if not exists)
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# Create logs table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        level TEXT,
        message TEXT
    )
""")

# Optional: Insert sample data
cursor.execute("""
    INSERT INTO logs (timestamp, level, message)
    VALUES (datetime('now'), 'INFO', 'Initial log entry')
""")

conn.commit()
conn.close()

print("✅ logs table created and sample entry added.")
