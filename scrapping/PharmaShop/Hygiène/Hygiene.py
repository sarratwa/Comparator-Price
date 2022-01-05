import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

PharmaShop_Hygiene_Product = []
c = 0
ProductLinks = []

for i in range(1,47):
    Site = requests.get("https://www.pharma-shop.tn/987-hygiene#/page-{}".format(i)).text
    soup = BeautifulSoup(Site,'html.parser')
    ProductList = soup.find_all("div",{"class":"product-container"})
    #print(ProductList)
    for Product in ProductList:
        link = Product.find("a",{"class":"product_img_link"}).get("href")
        ProductLinks.append(link)
#print(ProductLinks)

for link in ProductLinks:
    site2 = requests.get(link,headers=headers).text
    soup2=BeautifulSoup(site2, 'html.parser')
#Product_Name
    try:
        Product_Name = soup2.find("h1",{"itemprop":"name"}).text.replace("\n","")
    except:
        Product_Name = ("-")
#New_Price
    try:
        New_Price = soup2.find("span",{"id":"our_price_display"}).text.replace(" TTC","")
    except:
        New_Price = ("-")
#Old_Price
    try:
        Price = soup2.find("p",{"id":"old_price"}).text.replace(" TTC","")
        Old_Price = Price
    except:
        if Old_Price == "":
            Old_Price = ("-")        
#Discount
    try:
        Discount = soup2.find("p",{"id":"reduction_percent"}).text.replace(" ","")
    except:
        Discount = ("Pas Remise")
#Prd_Det
    try:
        Prod_Det = soup2.find("div",{"id":"more_info_sheets"}).text
    except:
        Prod_Det = ("-")

    PharmaShop = {"Produit":Product_Name, "Prix":New_Price, "Ancien prix":Old_Price, "Remise":Discount, "Description":Prod_Det, "Lien":link}
    PharmaShop_Hygiene_Product.append(PharmaShop)
    c += 1
    print("Completed",c)
    
PharmaShopHygieneProd = pd.DataFrame(PharmaShop_Hygiene_Product)

#To Excel
PharmaShopHygieneProd.to_excel("PharmaShop_Hygiene.xlsx",index=False)