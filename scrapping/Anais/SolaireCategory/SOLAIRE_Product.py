import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Anais_Solaire_Prod = []
c = 0
ProductLinks = []
for i in range(1,16):
    SolaireSite = requests.get("https://anais.tn/product-category/solaire/page/{}/".format(i)).text
    soup = BeautifulSoup(SolaireSite,'html.parser')
    ProductList = soup.find_all("div",{"class":"product-wrapper"})
    #print(ProductList)
    for Product in ProductList:
        link = Product.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get('href')
        ProductLinks.append(link)
#print(ProductLinks)
for link in ProductLinks:
    site = requests.get(link, headers=headers).text
    soup2 = BeautifulSoup(site,'html.parser')
#Product_Name
    try:
        Product_Name=soup2.find("h2",{"class":"product-name"}).text
    except:
        Product_Name = ("-")
#New_Price
    try:
        if soup2.find("del",{"class":"aria-hidden"}):
            New_Price = soup2.find("ins").text
        else:
            New_Price = soup2.find("span",{"class":"woocommerce-Price-amount amount"}).text
    except:
        New_Price = ("-")
#Old_Price
    try:
        Old_Price = soup2.find("del",{"aria-hidden":"true"}).text
    except:
        Old_Price = ("-")
#Links
    try:
        Links = soup2.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get('href')
    except:
        Links = ("-")
#Prod_Det
    try:
        Prod_Det = soup2.find("div",{"class":"woocommerce-product-details__short-description"}).text
    except:
        Prod_Det = ("-")
    Solaire = {"Produit":Product_Name, "Prix initiale":New_Price, "Ancien prix":Old_Price, "Description":Prod_Det, "Lien":Links}    
    Anais_Solaire_Prod.append(Solaire)
    c += 1
    print("Completed ",c)

AnaisAllProduct_Solaire= pd.DataFrame(Anais_Solaire_Prod)

#To Excel
AnaisAllProduct_Solaire.to_excel("Solaire_AnaisProduct.xlsx",index=False)
