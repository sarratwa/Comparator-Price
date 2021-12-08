import requests
from bs4 import BeautifulSoup
import pandas as pd

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
        Product_Name=soup2.find("h2", {"class":"woocommerce-loop-product__title"}).text
    except:
        Product_Name = ("-")
#New_Price
    try:
        if soup2.find("del",{"aria-hidden":"true"}):
            New_Price=soup2.find("ins").text
        else:
            New_Price=soup2.find("span", {"class":"woocommerce-Price-amount amount"}).text
    except:
        New_Price = ("-")
#Old_Price
    try:
        Old_Price=soup2.find("del",{"aria-hidden":"true"}).text
    except:
        Old_Price = ("-")
#Discount
    try:
        Discount=soup2.find("span", {"class":"label-sale"}).text
    except:
        Discount = ("Pas Remise")
#Links
    try:
        Links=soup2.find("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}).get('href')
    except:
        Links = ("-")
#Prod_Det
    try:
        Prod_Det=soup2.find("div",{"class":"woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab"}).text
    except:
        Prod_Det = ("-")
    
    Para = {"Produit":Product_Name, "Prix initiale":New_Price, "Ancien prix":Old_Price, "Remise":Discount, "Description":Prod_Det, "Lien":Links}
    Para_Promo.append(Para)
    c += 1
    print("Completed",c)

ParaPromoAllProduct = pd.DataFrame(Para_Promo)

#To Execl
ParaPromoAllProduct.to_excel("Produit_ParaPromo.xlsx",index=False)