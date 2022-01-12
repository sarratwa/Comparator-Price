import pymongo

# create mongodb client
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# create mongodb database
mydb = client['products']

data = mydb.prods

record = {
    "title": "Product #4",
    "price": "5,000 TN",
    "reduction": "-41%",
    "description": "bla bla bla",
    "link": "https://blablabla.com"
}

data.insert_one(record)
