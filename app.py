from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_html = mongo.db.mars_db.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_html)

# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    # Save the mars_db 
    mars_mongo = mongo.db.mars_db

    # Run the scrape function
    mars_info = scrape.scrape_all()
    
    # Update the Mongo database using update and upsert=True
    mars_mongo.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
