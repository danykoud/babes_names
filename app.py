from flask import Flask, render_template, request, jsonify, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect,join
from flask import (Flask, render_template, jsonify, request, redirect)
from flask_sqlalchemy import SQLAlchemy
import json
import collections
import pandas as pd 

######## INITIATE FLASK APP #########################
app= Flask(__name__)

engine= create_engine("postgres://uojmftnmharlnr:2afb0b29037d9b4cbf71fe7772cb4a0f499dad2c2133f74579a1f5d7cd3726da@ec2-54-160-202-3.compute-1.amazonaws.com:5432/d1rehkgcfdf1oa")

Base= automap_base()
Base.prepare(engine, reflect=True)
baby_names = Base.classes.baby_names
session = Session(engine)

#################################################
# Flask Routes
#################################################
@app.route ("/home")
@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/api/v1.0")
def show_apis():
    """List all available api routes."""
    return (
        f"<h2>CHOOSE YOUR ROUTE AND HAVE YOUR YOUR VISUAL:</h2>"

        f"<h4>Available Routes:</h4>"

        f'<a href="/home">home</a><br/>'
        f'<a href="/api/v1.0/graph">/api/v1.0/graph</a><br/>'
        f'<a href="/api/v1.0/gender">/api/v1.0/gender</a><br/>'
        f'<a href="/api/v1.0/Data">/api/v1.0/Data</a><br/>'        
    )  
@app.route("/graph")
def graph():

    return  render_template('map.html')

@app.route("/api/v1.0/gender")
def Gender_names():
    Fem_names= session.query(baby_names.Name,baby_names.Number ).filter(baby_names.Sex=="F").order_by(baby_names.Number.desc()).all()
    Male_names= session.query(baby_names.Name,baby_names.Number ).filter(baby_names.Sex=="F").order_by(baby_names.Number.desc()).all()
    Gender_F=[]
    Gender_M=[]
    for i in Male_names:
        Male_M={"Male_name":i.Name, "Male_number":i.Number}
        Gender_M.append( Male_M)
    for j in Fem_names:
        Fem_F={"Female_names":j.Name, "Female_Number":j.Number}
        Gender_F.append(Fem_F)
         
    return jsonify(Gender_F + Gender_M)
        

  
@app.route("/api/v1.0/Data")
def all_data():
    
    sel = [baby_names.Name, baby_names.State,baby_names.Sex, baby_names.Number,baby_names.Year, baby_names.Latitude,baby_names.Longitude,baby_names.City]
    results= session.query(*sel).filter(baby_names.Year >=1980 ).filter(baby_names.Year <=2018)
    data_map=[]
    for r in results:
        dict={"name":r.Name,"year":r.Year, "sex":r.Sex,"number":r.Number, "long":r.Longitude, "lat":r.Latitude, "state":r.City}
        data_map.append(dict)
    return jsonify(data_map)

if __name__ == '__main__':
    app.run(debug=True)