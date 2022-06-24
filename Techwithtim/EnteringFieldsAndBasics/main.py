# python-dotenv --> Will help us to access an enviroment variable file where we will store our credentials fro signing into MongoDB
from dotenv import load_dotenv,find_dotenv
# if we store information using enviroment variable then we
# will be able to share the code keeping the password secretly
# stored in our local machine

import os
import pprint
from pymongo import MongoClient

# find_dotenv() --> gives the path to .env file
# load_dotenv() --> loads the enviroment variable file for you 
# so you don't have to manually define the path and all that
load_dotenv(find_dotenv())

# This will take the value of env variable MONGODB_PWD and will 
# assign it to password os.environ.get() is a dictionary of 
# enviroment variables
password = os.environ.get("MONGODB_PWD")

# creating .env file to store passwords
connection_string = "mongodb+srv://SakshamVerma:{}@tutorial.usiuy.mongodb.net/?retryWrites=true&w=majority".format(password) 

# Connecting to database
client = MongoClient(connection_string)

# Getting a list of all the databases
# Connection.list_database_names()
print(client.list_database_names())

# Accessing a database Connection.databaseName
test_db = client.test

# Getting a list of all the collections in database test_db
# database.list_collection_names()
collections = test_db.list_collection_names()
print(collections)

def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name" : "Shubham",
        "type" : "Test"
    }

    # Inserting the document
    # collection.insert_one(test_document)
    
    # Getting the id of the collextion just inserted
    inserted_id = collection.insert_one(test_document).inserted_id

    print(inserted_id)

insert_test_doc()


# createDatabaseCollection

# Creating a database --> MongoDb automatically creates a database if not present
production = client.production

# Creating a collection --> MongoDb automatically creates a collection if not present
person_collection = production.person_collection

def create_documentsManyfields():
    first_names = ["Tim","Sarah","Jennifer","Jose","Brad","Allen"]

    last_names = ["Ruscica","Smith","Bart","Cater","Pit","General"]

    ages = [21,40,23,19,34,67]

    docs = []

    for first_name,last_name,age in zip(first_names,last_names,ages):
        doc = {"first_name" : first_name,"last_names" : last_names,"ages": ages}
        
        # Appending all dictionaries inside a list
        docs.append(doc)
    
    # Insert many fields inside the document at the same time
    person_collection.insert_many(docs)

def create_documentsOnefield():
    first_names = ["Tim","Sarah","Jennifer","Jose","Brad","Allen"]

    last_names = ["Ruscica","Smith","Bart","Cater","Pit","General"]

    ages = [21,40,23,19,34,67]

    for first_name,last_name,age in zip(first_names,last_names,ages):
        doc = {"first_name" : first_name,"last_names" : last_names,"ages": ages}

        person_collection.insert_one(doc)

create_documentsOnefield()