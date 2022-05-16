from pymongo import MongoClient
import json

connection_str = input("Please input the connection string: ")
client = MongoClient(connection_str) #creates a new MongoClient instance with specified connection string

db_name = input("Please input the database name: ")
db = client[db_name] #Accesses database using name as hashkey

collection_name = input("Please input the collection name: ")
collection = db[collection_name] #Accesses collection using name as hashkey

filepath_str = input("Please input filepath to JSON file: ")
with open(filepath_str, 'r') as f: #opens JSON file using specified path
    file_data = json.load(f) #converts data to JSON objects
    collection.insert_many(file_data) #inserts above JSON objects into the collection
        
client.close() #closes client connection
