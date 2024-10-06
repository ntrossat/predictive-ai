import sqlite3
from sqlalchemy import create_engine

from app import predict

db = sqlite3.connect("predictive_ai.db")
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


def run():
    predict.run()


if __name__ == "__main__":
    run()
