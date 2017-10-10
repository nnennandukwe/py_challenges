from pymongo import MongoClient

# calling the API for MongoDB
# make sure you've opened the terminal and gave the input command 'mongod'


Client = MongoClient()

# adding a database entry

db = Client["Library"]
collection = db["Books"]
book = {}

book['title'] = "Mongodb Guide"
book['year'] = 2018
book['Author'] = 'Ndukwe'

result = collection.insert_one(book)

print(book)