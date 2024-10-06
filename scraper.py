from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import requests
import re
import os

# display collected titles and page links
def dispArticleInfo(titles, links):
    for i in range(len(titles)):
        print(titles[i].text)
        # print(f"Section: {sections[i].text}")
        print(f"Link: {links[i].get('href')}\n")
        file.writelines(f"\n"+titles[i].text)
        # file.writelines(f"\nSection: {sections[i].text}")
        file.writelines(f"\nLink: {links[i].get('href')}\n")

year = '2009'
# prompt user to input a year
while (int(year) <= 2009 or int(year) > dt.now().year):
    year = input("Input a year no earlier than 2010: ") 
    if (int(year) <= 2009 or int(year) > dt.now().year):
        os.system('clear') 
        print("Please enter a valid year no earlier than 2010.")

URL  = 'https://thelasallian.com/'+year+'/page/1'
req  = requests.get(URL)
soup = bs(req.text, 'html.parser')
file = open(year+"-articles.txt", "w")

# find the max page count per year
pageCount = soup.find_all('a', class_='page-numbers')
pageCount = int(pageCount[-2].text)

for i in range(1,pageCount):
    URL = 'https://thelasallian.com/'+year+'/page/'+str(i)+'/'
    req  = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    
    titles = soup.find_all('h2', class_='entry-title heading-size-1')
    links  = soup.find_all('a', href=re.compile(year))
    # sections = soup.find_all('a', rel='category tag',
    # string=["University", "Menagerie", "Sports", "Vanguard", "Opinion"])
    print(f"Page {i}:") 
    file.writelines(f"\nPage {i}:") 
    dispArticleInfo(titles, links)

file.close()
