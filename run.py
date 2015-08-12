# Regular python imports
import os

# Library imports
import googlemaps
import pymongo
from pyjade import html

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

def closest_events(origin_zip, pending_or_scheduled):
    events = mongo_client.hosts[pending_or_scheduled].find()
    return maps_client.distance_matrix(origin_zip, destination_address)

# ---------- BASIC STATIC HTML SERVING ----------
@app.route("/")
def home():
    return send_file('./html/index.html')

@app.route("/participate.html")
def participate():
    return send_file('./html/participate.html')

@app.route("/host.html")
def host():
    return send_file('./html/host.html')

@app.route("/partner.html")
def partner():
    return send_file('./html/partner.html')

@app.route("/think.html")
def think():
    return send_file('./html/think.html')

@app.route("/about.html")
def about():
    return send_file('./html/about.html')

# ---------- SERVE IMAGES ----------
@app.route("/images/<imagename>")
def serve_image(imagename):
    return send_file("./images/" + imagename)

# ---------- SERVE CSS ----------
@app.route("/css/<stylename>")
def serve_css(stylename):
    return send_file("./css/" + stylename)

# def build_app():
#     # Jade to html
#     print 'Building jade...'
#     for jd in os.listdir('./jade'):
#         fn = jd.split('.')
#         if fn[1] == 'jade':
#             out = open('./html/%s.html' % fn[0], 'w')
#             out.write(html.process_jade(open('./jade/%s' % jd).read()))
#     print '...jade built.'
#     print 'Building styl...'


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
    # build_app()
    app.run(debug=True)



