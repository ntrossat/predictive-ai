import click
import sqlite3
from sqlalchemy import create_engine

db = sqlite3.connect("predictive_ai.db")
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@click.command()
@click.option("--name", help="Your name", default="World")
def run(name):
    print(f"Hello, {name}!")
