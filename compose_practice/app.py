import os
import time
import psycopg2


def connect():
    for _ in range(10):
        try:
            return psycopg2.connect(
                host=os.environ["DB_HOST"],
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
            )
        
        except psycopg2.OperationalError:
            print("Waiting for the database...")
            time.sleep(2)
            
    raise SystemExit("Could not connect to the database")


conn = connect()
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name TEXT, marks INT)")
cur.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", ("Hamza", 90))
conn.commit()


cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()