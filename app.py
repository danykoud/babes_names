from config import database, connect_string
from BabiesNamesData import BabiesNamesData
from flask import Flask, jsonify, render_template

######## INITIATE FLASK APP #########################
app= Flask(__name__)
app.static_folder = 'static'

db= BabiesNamesData()
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
@app.route("/api/v1.0/Data")
def get_data():
    
    return jsonify(db.get_all_data)

if __name__ == '__main__':
    app.run(debug=True)






