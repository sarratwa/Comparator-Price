from requests_html import HTMLSession
import pandas as pd
url = 'https://anais.tn/product-category/materiel-medical/'
s = HTMLSession()
c = 0

def get_links(url):
    r = s.get(url)
    items = r.html.find('div.product-wrapper')
    links = []
    for item in items:
        links.append(item.find('a', first=True).attrs['href'])
    return links

def get_Product(link):
    r = s.get(link)
    Product_Name = r.html.find('h1',first=True).full_text
    Price = r.html.find('p')[1].full_text
    Prod_Desc = r.html.find('div.woocommerce-product-details__short-description ul')[0].full_text.replace('\n','')
    Category = r.html.find('a[rel=tag]', first=True).full_text
    
    Product = {'Nom Produit':Product_Name,'Prix':Price,'Description':Prod_Desc,'Categorie':Category,"Lien":link}
    return Product

links = get_links(url)
results = []
for link in links:
    results.append(get_Product(link))
    c += 1
    print("Completed ",c)

MatMed=pd.DataFrame(results)
print(MatMed)
#MatMed.to_excel("MaterielMedical_AnaisProduct.xlsx",index=False)
