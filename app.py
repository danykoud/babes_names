from flask import Flask, render_template, request, jsonify, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect,join
from flask import (Flask, render_template, jsonify, request, redirect)
from flask_sqlalchemy import SQLAlchemy
import json
import collections

######## INITIATE FLASK APP #########################
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://uojmftnmharlnr:2afb0b29037d9b4cbf71fe7772cb4a0f499dad2c2133f74579a1f5d7cd3726da@ec2-54-160-202-3.compute-1.amazonaws.com:5432/d1rehkgcfdf1oa'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class baby_names(db.Model):
    __tablename__ = 'baby_names'
    id = db.Column(db.Integer, primary_key=True)
    State= db.Column(db.String(200))
    Sex = db.Column(db.String(20))
    Year = db.Column(db.Integer)
    Name = db.Column(db.String(200))
    Number = db.Column(db.Integer)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    City = db.Column(db.String(200))

    def __init__(self, State, Sex, Year, Name, Latitude, Longitude,City):
        self.State = State
        self.Sex =Sex
        self.Year = Year
        self.Name = Name
        self.Latitude = Latitude
        self.Longitude = Longitude
    
    def __repr__(self):

        return '<babynames_us %r>' % (self.Name)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return  render_template('index.html')

@app.route("/api/v1.0")
def show_apis():
    """List all available api routes."""
    return (
        f"<h4>Available Routes:</h4>"
        f'<a href="/api/v1.0/Data">/api/v1.0/Data</a><br/>'        
    )    
@app.route("/api/v1.0/Data", methods=["GET", 'POST'])
def all_data():
    sel = [baby_names.Name, baby_names.State,baby_names.Sex, baby_names.Number,baby_names.Year, baby_names.Latitude,baby_names.Longitude,baby_names.City]
    results= db.session.query(*sel).filter(baby_names.Year >=1980 ).filter(baby_names.Year <=2018)
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
