from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import requests, re, os 

# Get each article's section categories
# @param sectionContainers 
# - The list of HTML elements holding the sections for each article.
# @param artNum 
# - The index of the article in the list of sectionContainers.
#
# @return The section(s) associated with the given article.
def getSections(sectionContainers, artNum):
    sectionList = sectionContainers[artNum].find_all(
        'a', rel='category tag'
    )
    if (len(sectionList) == 1): return sectionList[0].text
    return sectionList[0].text + " & " + sectionList[1].text 

# Print the article's title, link, and section category 
# via terminal and text file output
# 
# @param titles 
# - The list of HTML elements containing the titles of the articles.
# @param links 
# - The list of HTML elements containing the links to the articles.
# @param sectionContainers 
# - The list of HTML containers holding the sections for each article.
#
# @return none
def dispArticleInfo(titles, links, sectionContainers):
    for i in range(len(titles)): 
        sections = getSections(sectionContainers, i)  
        print(titles[i].text)
        print(f"Section: {sections}")
        print(f"Link: {links[i].get('href')}\n")
        
        file.writelines(f"\n"+titles[i].text)
        file.writelines(f"\nSection: {sections}")
        file.writelines(f"\nLink: {links[i].get('href')}\n")

year = '2009'
# Prompt the user to input a valid year (no earlier than 2010) until a valid input is provided.
while (int(year) <= 2009 or int(year) > dt.now().year):
    year = input("Input a year no earlier than 2010: ") 
    if (int(year) <= 2009 or int(year) > dt.now().year):
        os.system('clear') 
        print("Please enter a valid year no earlier than 2010.")

URL  = 'https://thelasallian.com/'+year+'/page/1'
req  = requests.get(URL)
soup = bs(req.text, 'html.parser')
file = open(year+"-articles.txt", "w")

# Find the maximum number of pages of articles for the given year 
pageCount = soup.find_all('a', class_='page-numbers')
pageCount = int(pageCount[-2].text)+1

# Loop through each page of articles for the specified year.
for i in range(1, pageCount):
    URL  = 'https://thelasallian.com/'+year+'/page/'+str(i)+'/'
    req  = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    
    titles = soup.find_all('h2', class_='entry-title heading-size-1')
    sectionContainers = soup.find_all(class_="entry-categories-inner")
    links  = soup.find_all('a', href=re.compile(year))
    
    print(f"Page {i}:") 
    file.writelines(f"\nPage {i}:") 
    
    dispArticleInfo(titles, links, sectionContainers)

file.close()
