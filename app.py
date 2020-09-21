import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect,join
from flask import (Flask, render_template, jsonify, request, redirect)
from flask_sqlalchemy import SQLAlchemy
import json
import collections
import pandas as pd 
import numpy as np 

######## INITIATE FLASK APP #########################
app= Flask(__name__)

engine = create_engine('postgres://uojmftnmharlnr:2afb0b29037d9b4cbf71fe7772cb4a0f499dad2c2133f74579a1f5d7cd3726da@ec2-54-160-202-3.compute-1.amazonaws.com:5432/d1rehkgcfdf1oa')

Base= automap_base()
Base.prepare(engine, reflect=True)
baby_names = Base.classes.baby_names
session = Session(engine)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return  render_template('index.html')
@app.route("/graph")
def graph():
    return  render_template('map.html')
@app.route("/api/v1.0")
def show_apis():
    """List all available api routes."""
    return (
        f"<h4>Available Routes:</h4>"
        f'<a href="/api/v1.0/Data">/api/v1.0/Data</a><br/>'        
    )    
@app.route("/api/v1.0/Data")
def all_data():
    sel = [baby_names.Name, baby_names.State,baby_names.Sex, baby_names.Number,baby_names.Year, baby_names.Latitude,baby_names.Longitude,baby_names.City]
    results= session.query(*sel).filter(baby_names.Year >=1980 ).filter(baby_names.Year <=2018)
    all_data=[]
    for result in results:
        d = collections.OrderedDict()
        d["Name"]=result[0]
        d["State"]=result[1]
        d["Sex"]=result[2]
        d["Number"]=result[3]
        d["Year"]=result[4]
        d["Latitude"]=result[5]
        d["Longitude"]=result[6]
        d["City"]=result[7]
        # r= result[0] + result[0] + result[0] + result[0] + result[0] + result[0] + result[0] + result[0]
        all_data.append(d)
        json.dumps(all_data)
        # with open("static/js/covid_data.js", "w") as f:
        #     f.write(covid_json)
    return jsonify('all_data')

if __name__ == '__main__':
    app.run(debug=True)
