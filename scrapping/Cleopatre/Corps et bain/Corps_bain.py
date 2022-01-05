import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Cleopatre_Visage_Product = []
c = 0
ProductLinks = []

for i in range(1,15):
    Site = requests.get('https://www.cleopatre.tn/33-corps-et-bain?page={}'.format(i)).text
    soup = BeautifulSoup(Site, 'html.parser')
    ProductList = soup.find_all("div",{"class":"item-product col-xs-12 col-sm-6 col-md-6 col-lg-4 col-xl-3"})
    #print(ProductList)

    for Product in ProductList:
        link = Product.find("a",{"class":"thumbnail product-thumbnail"}).get('href')
        ProductLinks.append(link)
#print(ProductLinks)

for link in ProductLinks:
    site2 = requests.get(link,headers=headers).text
    soup2=BeautifulSoup(site2, 'html.parser')
#Product_Name
    try:
        Product_Name=soup2.find("h1", {"class":"h1 namne_details"}).text
    except:
        Product_Name = ("-")
#New_Price
    try:
        New_Price = soup2.find("span",{"class":"price"}).text
    except:
        New_Price = ("-")
#Old_Price
    try:
        Old_Price = soup2.find("span",{"class":"regular-price"}).text
    except:
        Old_Price = ("-")
#Discount
    try:
        Discount=soup2.find("span", {"class":"discount discount-percentage"}).text
    except:
        Discount = ("Pas Remise")
#Prod_Det
    try:
        Prod_Det=soup2.find("div",{"class":"product-description"}).text
    except:
        Prod_Det = ("-")
    
    Cleopatre = {"Produit":Product_Name, "Prix actuel":New_Price, "Ancien prix":Old_Price, "Remise":Discount, "Description":Prod_Det, "Lien":link}
    Cleopatre_Visage_Product.append(Cleopatre)
    c += 1
    print("Completed",c)

CleopatreAllProduct = pd.DataFrame(Cleopatre_Visage_Product)

#To Execl
CleopatreAllProduct.to_excel("Produit_Cleopatre.xlsx",index=False)