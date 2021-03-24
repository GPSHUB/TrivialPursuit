import flask
import pandas as pd
import sqlalchemy
import joblib
# import numpy as np
# import plotly as plt
# import matplotlib.pyplot as plt
# import plotly.express as px
from flask import Flask, jsonify, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, TextAreaField, IntegerField, FloatField
# from wtforms.validators import DataRequired
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
# from sklearn.datasets import make_regression
# from sklearn.linear_model import LinearRegression

engine = create_engine("sqlite:///trivia_db.db")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1.0/login_table")
def login():
    session = Session(engine)
    results = trivia_db.session.query(trivia_db.login_table.all())

    return jsonify(results)
    session.close()

if __name__ == "__main__":
    app.run()






