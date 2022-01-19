import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Anais_MatMedical_Prod = []
c = 0
ProductLinks = []
for i in range(1,2):
    MatMedicalSite = requests.get("https://anais.tn/product-category/materiel-medical/".format(i)).text
    soup = BeautifulSoup(MatMedicalSite,'html.parser')
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
#Image
    try:
        Image = soup2.find("a",{"class":"woocommerce-main-image zoom"})['href']
    except:
        Image = ("-")

    MatMedical = {"title":Product_Name, "price":Price, "description":Prod_Det, "link":link, "Image":Image, "categorie":"Autre"}
    Anais_MatMedical_Prod.append(MatMedical)
    c += 1
    print("Completed ",c)

AnaisAllProduct_MatMedical = pd.DataFrame(Anais_MatMedical_Prod)

#To Excel
AnaisAllProduct_MatMedical.to_csv("MatMedical_AnaisProduct.csv",index=False)
