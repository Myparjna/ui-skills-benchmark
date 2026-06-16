import sqlite3
db_path = r'C:\Users\mypra\.local\share\mimocode\mimocode.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cursor.fetchall()]
print("Tables:", tables)

# Row counts
for t in tables:
    try:
        cursor.execute(f"SELECT COUNT(*) FROM [{t}]")
        count = cursor.fetchone()[0]
        print(f"  {t}: {count} rows")
    except Exception as e:
        print(f"  {t}: ERROR - {e}")

# Show schema for key tables
for t in ['session', 'message', 'part', 'task', 'task_event', 'actor_registry']:
    if t in tables:
        cursor.execute(f"PRAGMA table_info([{t}])")
        cols = cursor.fetchall()
        print(f"\n--- {t} schema ---")
        for c in cols:
            print(f"  {c[1]} ({c[2]})")

conn.close()
