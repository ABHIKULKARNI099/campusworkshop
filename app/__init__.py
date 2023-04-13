"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq0c1mbg5e4khpuq3g-a.oregon-postgres.render.com",
        database="todo_7v4c",
        user="root",
        password="HEPrFqxp9tqQwf4Zu0FPQT1vdDvbbnE3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
