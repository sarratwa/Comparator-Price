import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import json

#connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

#read csv file
df = pd.read_csv('ParaPharmacie.csv')

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
db.ParaPharmacie.insert_many(data)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

ParaPharmacie_Product = []
c = 0
ProductLinks = []

for i in range(1,194):
    Site = requests.get("https://parapharmacie.tn/boutique/page/{}/".format(i)).text
    soup = BeautifulSoup(Site,'html.parser')
    ProductList = soup.find_all("div",{"class":"product-inner"})
    #print(ProductList)
    for Product in ProductList:
        link = Product.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get('href')
        ProductLinks.append(link)
#print(ProductLinks)

for link in ProductLinks:
    site2 = requests.get(link,headers=headers).text
    soup2=BeautifulSoup(site2, 'html.parser')
#Product_Name
    try:
        Product_Name = soup2.find("h1",{"class":"product_title entry-title"}).text
    except:
        Product_Name = ("-")
#Price
    try:
        Price = soup2.find("p",{"class":"price"}).text
    except:
        Price = ("-")      
#Prd_Det
    try:
        Prod_Det = soup2.find("div",{"class":"woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab"}).text
    except:
        Prod_Det = ("-")
#Image
    try:
        Image = soup2.find("img",{"class":"attachment-woocommerce_thumbnail size-woocommerce_thumbnail"}).get('src')
    except:
        Image = ("-")

    ParaPharmacie = {"titre":Product_Name, "Price":Price, "description":Prod_Det, "Link":link, "Image":Image}
    ParaPharmacie_Product.append(ParaPharmacie)
    c += 1
    print("Completed",c)
    
ParaPharmacieProd = pd.DataFrame(ParaPharmacie_Product)

#To Excel
ParaPharmacieProd.to_csv("ParaPharmacie.csv",index=False)