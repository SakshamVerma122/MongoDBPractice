from dotenv import load_dotenv,find_dotenv
import os
from pymongo import MongoClient

# find_dotenv() --> gives the path to .env file
# load_dotenv() --> loads the enviroment variable file for you 
# so you don't have to manually define the path and all that
load_dotenv(find_dotenv())

# Getting Password from enviroment variable
password = os.environ.get("MONGODB_PWD")
connection_string = "mongodb+srv://SakshamVerma:{}@tutorial.usiuy.mongodb.net/?retryWrites=true&w=majority".format(password) 

# Connecting to database
client = MongoClient(connection_string)

connection_string = "mongodb+srv://SakshamVerma:{}@tutorial.usiuy.mongodb.net/?retryWrites=true&w=majority".format(password) 

# Connecting to database
client = MongoClient(connection_string)
