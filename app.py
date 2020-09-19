from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"<h4>Available Routes:</h4>"
        f'<a href="/api/v1.0/ids">/api/v1.0/ids</a><br/>'
        f'<a href="/api/v1.0/info/1286">/api/v1.0/info/subject_id</a><br/>'
        f'<a href="/api/v1.0/subjects">/api/v1.0/subjects</a><br/>'
        f'<a href="/api/v1.0/subjects/1286">/api/v1.0/subjects/subject_id</a><br/>'
        f'<a href="/"><h4>Back</h4></a><br/>'
    )
























# # import necessary libraries

# import os
# from flask import (
#     Flask,
#     render_template,
#     jsonify,
#     request,
#     redirect)
# from flask_sqlalchemy import SQLAlchemy




# # Flask Setup
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return ("hello word")
# if __name__ == "__main__":
#     app.run()

# ENV = 'prod'

# if ENV == 'dev':

#     app.debug = True

#     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:Koudede$89@localhost:5432/babynames_db"
#     # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///babynames_db"
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''
    
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# reflect the existing base into a new model 
# def create_classes(db):
#     class names(db.Model):
#         __tablename__ = 'baby_names'
        
#         id = db.Column(db.Integer, primary_key=True)
#         state = db.Column(db.String(64))
#         sex = db.Column(db.String(10))
#         year = db.Column(db.Float)
#         name = db.Column(db.String(64))
#         number = db.Column(db.Float)
        
#         def __init__(self,state,sex,year, name,number):

#             self.state = state
#             self.sex = sex
#             self.year = year
#             self.name = name
#             self.number = number
       
#         def __repr__(self):
#             return '<names %r>' % (self.name)
    




# names = create_classes(db)


# # create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/Data")
# def home():
#     return render_template("data.html")

# @app.route("/data/name")
# def data():
#     results = db.session.query(names.name, names.number, names.sex, names.state).all()


#     names_array = []
#     for result in results:

#         c = {}

#         c["name"] = result[0]
#         c["number"] = result[1]
#         c["sex"] = result[2]
#         c["state"] = result[3]

#         names_array.append(c)
#     return jsonify(names_array)
    
# if __name__ == "__main__":
#     app.run()

