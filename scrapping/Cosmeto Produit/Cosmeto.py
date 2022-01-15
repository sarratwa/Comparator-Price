import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.cosmeto.tn/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

Cosmeto = []
c = 0
ProductLinks = []


for i in range(1,40):
    Site = requests.get('https://www.cosmeto.tn/shop/page/{}/'.format(i)).text
    soup = BeautifulSoup(Site, 'html.parser')
    ProductList = soup.find_all("ul",{"class":"products columns-6 hongo-shop-standard hongo-shop-common-isotope hongo-product-list-common-wrap hongo-shop-col-6 hongo-shop-md-col-4 hongo-shop-sm-col-4 hongo-shop-xs-col-1 gutter-large hongo-buttons-1 hongo-text-center"})
      
for Product in ProductList:
        link = Product.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get("href")
        ProductLinks.append(link)
#print(ProductLinks)

for i in range(1,43):
    Site = requests.get('https://www.cosmeto.tn/shop/page/{}/'.format(i)).text
    soup = BeautifulSoup(Site, 'html.parser')
    ProductList = soup.find_all("div",{"class":"product-thumb-wrap"})
    #print(ProductList)   

    for Product in ProductList:
        link = Product.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get("href")
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
    Cos = {"Produit":Prodcut_Name, "Prix":Price, "Description":Prod_det, "Lien":link}
    Cosmeto.append(Cos)
    c += 1
    print ("Completed", c)

CosmetoAllProduct = pd.DataFrame(Cosmeto)

#To Excel
CosmetoAllProduct.to_excel("Produit_Cosmeto.xlsx",index=False)