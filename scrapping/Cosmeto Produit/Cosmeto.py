import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import json

#connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

#read csv file
df = pd.read_csv('Produit_Cosmeto.csv.csv')

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
db.Cosmeto.insert_many(data)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Cosmeto = []
c = 0
ProductLinks = []

for i in range(1,2):
    Site = requests.get('https://www.cosmeto.tn/shop/page/{}/'.format(i)).text
    soup = BeautifulSoup(Site, 'html.parser')
    ProductList = soup.find_all("div",{"class":"product-thumb-wrap"})
    #print(ProductList)

    for Product in ProductList:
        link = Product.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get('href')
        ProductLinks.append(link)
#print(ProductLinks)


for link in ProductLinks:
    CosmoSite = requests.get(link,headers=headers).text
    soup2 = BeautifulSoup(CosmoSite, 'html.parser')
#Product_Name
    try:
        Prodcut_Name = soup2.find("h1",{"class":"product_title entry-title alt-font"}).text
    except:
        Prodcut_Name = ("-")
#Price
    try:
        Price = soup2.find("p",{"class":"price alt-font"}).text
    except:
        Price = ("-")
#Prod_Det
    try:
        Prod_det = soup2.find("div",{"class":"woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab"}).text
    except:
        Prod_det = ("-")
#Image
    try:
        Image = soup2.find("div",{"class":"woocommerce-product-gallery__image"}).get('data-thumb')
    except:
        Image = ("-")

    Cos = {"title":Prodcut_Name, "price":Price, "description":Prod_det, "link":link, "Image":Image}
    Cosmeto.append(Cos)
    c += 1
    print ("Completed", c)

CosmetoAllProduct = pd.DataFrame(Cosmeto)

#To Excel
CosmetoAllProduct.to_csv("Produit_Cosmeto.csv",index=False)