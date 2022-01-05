import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Cleopatre_Puericulture_Product = []
c = 0
ProductLinks = []

for i in range(1,10):
    Site = requests.get('https://www.cleopatre.tn/41-puericulture?page={}'.format(i)).text
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
        Product_Name=soup2.find("h1",{"class":"h1 namne_details"}).text
    except:
        Product_Name = ("-")
#New_Price
    try:
        New_Price = soup2.find("span",{"class":"price"}).text
    except:
        New_Price = ("-")
#Old_Price
    try:
        Old_Price = soup2.find("div",{"class":"product-discount"}).text
    except:
        Old_Price = ("-")
#Discount
    try:
        Discount=soup2.find("span",{"class":"discount discount-percentage"}).text
    except:
        Discount = ("Pas Remise")
#Prod_Det
    try:
        Prod_Det=soup2.find("div",{"class":"product-desc"}).text.replace("\n\n","")
    except:
        Prod_Det = ("-")
    
    Cleopatre = {"Produit":Product_Name, "Prix actuel":New_Price, "Ancien prix":Old_Price, "Remise":Discount, "Description":Prod_Det, "Lien":link}
    Cleopatre_Puericulture_Product.append(Cleopatre)
    c += 1
    print("Completed",c)

PuericultureAllProduct = pd.DataFrame(Cleopatre_Puericulture_Product)

#To Execl
PuericultureAllProduct.to_excel("Produit_PuericultureCleopatre.xlsx",index=False)