import os

import psycopg
from fastapi import FastAPI

app = FastAPI()
DSN = os.environ["DATABASE_URL"]


@app.get("/")
def root():
    with psycopg.connect(DSN) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS hits "
            "(id serial PRIMARY KEY, at timestamptz DEFAULT now())"
        )
        conn.execute("INSERT INTO hits DEFAULT VALUES")
        count = conn.execute("SELECT count(*) FROM hits").fetchone()[0]
    return {"hits": count}
