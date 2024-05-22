from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize the PyMongo extension
mongo = PyMongo(app)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Import and register the routes
from app import routes
