from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#  Flask Setup
app = Flask(__name__)


# PyMongo Connection Setup

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
       # Return template and data
    return render_template("index.html", mars=mars)
# Route that will trigger the scrape function
@app.route("/scrape")
def scrapper():
     # Run the scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
   print(scrape_all())