import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import json

#connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

#read csv file
df = pd.read_csv('Produit_ParaPromo.csv')

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
db.ParaPromo.insert_many(data)


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Para_Promo = []
c = 0
ProductLinks = []

for i in range(1,50):
    Site = requests.get('https://para-promo-tunisie.com/parapharmacie-tunisie/page/{}/'.format(i)).text
    soup = BeautifulSoup(Site, 'html.parser')
    ProductList = soup.find_all("div",{"class":"product-wrapper gridview"})
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
        Product_Name=soup2.find("h1", {"class":"product_title entry-title"}).text
    except:
        Product_Name = ("-")
#Price
    try:
        Price = soup2.find("p",{"class":"price"}).text
    except:
        Price = ("-")
#Discount
    try:
        Discount=soup2.find("span", {"class":"label-sale"}).text
    except:
        Discount = ("Pas Remise")
#Prod_Det
    try:
        Prod_Det=soup2.find("div",{"class":"woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab"}).text
    except:
        Prod_Det = ("-")
#Image
    try:
        Image = soup2.find("a",{"class":"yith_magnifier_zoom woocommerce-main-image"})['href']
    except:
        Image = ("-")
    Para = {"Produit":Product_Name, "Prix":Price, "Remise":Discount, "Description":Prod_Det, "Lien":link, "Image":Image}
    Para_Promo.append(Para)
    c += 1
    print("Completed",c)
    
ParaPromoAllProduct = pd.DataFrame(Para_Promo)

#To Execl
ParaPromoAllProduct.to_csv("Produit_ParaPromo.csv")