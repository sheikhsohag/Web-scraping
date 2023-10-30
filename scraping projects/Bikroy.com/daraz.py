from bs4 import BeautifulSoup
import requests

def Daraz():
    url = "https://bikroy.com/en/ads?query=laptop"
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text,'lxml')
    # print(soup)
    laptops=soup.find_all('li', class_="normal--2QYVk gtm-normal-ad")
    for index, laptop in enumerate(laptops):
        name = laptop.find('h2', class_='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow').text
        location = laptop.find('div',class_='description--2-ez3').text
        price = laptop.find('div',class_='price--3SnqI color--t0tGX').span.text 
        more_details = laptop.find('a', class_='card-link--3ssYv gtm-ad-item').get('href')
        with open(f'Bikroy.com/{index}.txt','w',encoding='utf-8') as f:
            f.write(f"Laptop Name: {name.strip()}\n")
            f.write(f"Location: {location.strip()}\n")
            f.write(f"Price: {price.strip()}\n")
            f.write(f"More Details: {more_details.strip()}\n")
        print(f'File saved: {index}')
                
    

Daraz()