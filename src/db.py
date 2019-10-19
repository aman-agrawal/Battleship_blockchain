from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.amandb
print(db.list_collection_names())

#making-a-connection-with-mongoclient
#	https://api.mongodb.com/python/current/tutorial.html