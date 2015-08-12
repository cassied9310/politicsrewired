# Regular python imports
import os

# Library imports
import googlemaps
import pymongo

# Flask imports
from flask import Flask
from flask import send_file
app = Flask(__name__)

try:
    MONGO_URL = os.environ['MONGO_URL']
except:
    MONGO_URL = 'mongodb://localhost:27017/'
try:
    GOOGLEMAPS_API_KEY = os.environ['GOOGLEMAPS_API_KEY']
except:
    GOOGLEMAPS_API_KEY = ""
try:
    TYPEFORM_API_KEY = os.environ['TYPEFORM_API_KEY']
except:
    TYPEFORM_API_KEY = ""



@app.route("/")
def home():
    return open('./index.html','r').read()

@app.route("/images/<imagename>")
def serve_image(imagename):
    return send_file("./images/" + imagename)

@app.route("/css/<stylename>")
def serve_css(stylename):
    return send_file("./css/" + stylename)

def closest_events(origin_zip, pending_or_scheduled):
    events = mongo_client.hosts[pending_or_scheduled].find()
    return maps_client.distance_matrix(origin_zip, destination_address)

if __name__ == "__main__":
    # Configure Google Maps client
    # maps_client = googlemaps.Client(key=GOOGLEMAPS_API_KEY)

    # Configure MongoDB client
    # mongo_client = pymongo.MongoClient(MONGO_URL)
    # Insert necessary collections
    # db = mongo_client.participants
    # db = mongo_client.sponsors
    # db = mongo_client.hosts
    # db = mongo_client.hosts.pending
    # db = mongo_client.hosts.scheduled

    app.run()



