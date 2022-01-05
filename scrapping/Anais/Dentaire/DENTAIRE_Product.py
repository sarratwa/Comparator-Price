import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Anais_Dentaire_Prod = []
c = 0
ProductLinks = []
for i in range(1,7):
    DentaireSite = requests.get("https://anais.tn/product-category/dentaire/page/{}/".format(i)).text
    soup = BeautifulSoup(DentaireSite,'html.parser')
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
        Product_Name=soup2.find("h1",{"class":"product_title entry-title"}).text
    except:
        Product_Name = ("-")
#Price
    try:
        Price = soup2.find("p",{"class":"price"}).text
    except:
        Price = ("-")
#Prod_Det
    try:
        Prod_Det = soup2.find("div",{"class":"woocommerce-product-details__short-description"}).text
    except:
        Prod_Det = ("-")

    Dentaire = {"Produit":Product_Name, "Prix":Price, "Description":Prod_Det, "Lien":link}    
    Anais_Dentaire_Prod.append(Dentaire)
    c += 1
    print("Completed ",c)

AnaisAllProduct_Dentaire = pd.DataFrame(Anais_Dentaire_Prod)

#To Excel
AnaisAllProduct_Dentaire.to_excel("Dentaire_AnaisProduct.xlsx",index=False)