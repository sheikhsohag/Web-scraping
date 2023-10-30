from bs4 import BeautifulSoup
import requests
import time


def Daraz_web_scraping():
    html_text = requests.get('https://internshala.com/jobs/').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs=soup.find_all('div', class_='internship_meta')
    
                       
    for index, job in enumerate(jobs):
        company_name = job.find('h3',class_='heading_4_5 profile').text
        experience = job.find('div',class_='item_body mobile-text').text
        salary = job.find('span', class_='mobile').text
        location = job.find('a',class_='location_link view_detail_button').text
        post_date = job.find('div', class_='status status-small status-inactive').text
        details = job.find('a', class_='view_detail_button')
        detail = details.get('href')
        
        with open(f'internshala/{index}.txt','w',encoding='utf-8') as f:
            f.write(f"Company Name: {company_name.strip()}\n")
            f.write(f"Post Date : {post_date.strip()}\n")
            f.write(f"Salary : {salary.strip()}\n")
            f.write(f"Experience : {experience.strip()}\n")
            f.write(f"Locatin : {location.strip()}\n")
            f.write(f"More Details: {detail.strip()}\n")
        print(f'File saved: {index}')    
                   
Daraz_web_scraping()