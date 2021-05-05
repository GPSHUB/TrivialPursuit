import flask
import pandas as pd
import sqlalchemy
import joblib
from flask import Flask, jsonify, render_template, request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///trivia_db.db")

app = Flask(__name__)

login_list = pd.read_sql('SELECT * FROM login_table', con = engine)
scoring_list = pd.read_sql('SELECT * FROM scoring_table', con = engine)
question_list = pd.read_sql('SELECT * FROM question_table', con = engine)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1.0/login_table")
def login_table():
    session = Session(engine)
    results = login_list.to_dict('records')
    return jsonify(results)    
    session.close()

@app.route("/api/v1.0/scoring_table")
def scoring_table():
    session = Session(engine)
    results2 = scoring_list.to_dict('records')
    return jsonify(results2)
    session.close()

@app.route("/api/v1.0/question_table")
def question_table():
    session = Session(engine)
    results3 = question_list.to_dict('records')
    return jsonify(results3)
    session.close()

if __name__ == "__main__":
    app.run()






