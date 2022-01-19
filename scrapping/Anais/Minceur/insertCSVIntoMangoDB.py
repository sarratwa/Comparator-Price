import pymongo
import pandas as pd
import json

#connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

#read csv file
df = pd.read_csv('Minceur_AnaisProduct.csv')

#data frame
# print(df.head())

#tail of data frame
# print(df.tail())

#shape of data frame
# print(df.shape)

#convert csv to json because mongodb stores in the form of json
data = df.to_dict(orient = 'records')
# print(data)

#database
db = client['products']

# print(db)

#save records in this database
db.prods.insert_many(data)