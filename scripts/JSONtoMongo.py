from pymongo import MongoClient
import json
import glob


HOST = 'localhost'
PORT = '27107'

url = f"mongodb://{HOST}:{PORT}/"
client = MongoClient()

client.drop_database('eddo')
db_name = 'eddo'
db = client[db_name]

files = glob.glob('./data/*.json')

for file in files:
    collection_name = file[7:-5]
    collection = db[collection_name]
    json_text = open(file, 'r').read()
    json_obj = json.loads(json_text)
    collection.insert_many(json_obj)

client.close()