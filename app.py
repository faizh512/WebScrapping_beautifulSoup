import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the webpage
webpage = requests.get(url='https://www.thenews.com.pk/latest/category/sports')
if webpage.status_code == 200:
    print("Successfully fetched HTML")
else:
    print(f"We can't access the HTML code due to that error {webpage.status_code}")

# Parse the HTML content
soup = BeautifulSoup(webpage.content, 'html.parser')
li_tags = soup.findAll('li')

# Initialize lists to store data
h2 = []
p = []
date = []
image = []
links = []
detail=[]
# Extract data from the HTML
for li in li_tags:
    h2_tag = li.find('h2')
    p_tag = li.find('p')
    date_tag = li.find('span')
    img_tag = li.find('img')
    a_tag = li.find('a',class_=["open-section" ,"latest-page-img"])  # Find the first <a> tag within the <li>
   
    # next_page = requests.get(url=a_tag.get('href'))
    # if next_page.status_code == 200:
    #     print("Successfully fetched HTML")
    #     print(a_tag.get('href'))
    if h2_tag and p_tag and date_tag and img_tag and a_tag:
        h2.append(h2_tag.text)
    if h2_tag and p_tag and date_tag and img_tag and a_tag:
        p.append(p_tag.text)
    if h2_tag and p_tag and date_tag and img_tag and a_tag:
        date.append(date_tag.text)
    if h2_tag and p_tag and date_tag and img_tag and a_tag:
        img_src = img_tag.get('src')
        if img_src:
            image.append(img_src)
    if h2_tag and p_tag and date_tag and img_tag and a_tag:
        href = a_tag.get('href')
        if href:
            discription=str()
            links.append(href)
            next_page=requests.get(href)
            soup = BeautifulSoup(next_page.content, 'html.parser')
            div_tag=soup.find('div',class_='story-detail')
            p_tags =div_tag.findAll('p')
            for i in p_tags:
                discription=discription+"\n"+str(i.text)
            detail.append(discription)
        else:
            links.append(None)
 

# Ensure all lists are of equal length
max_len = max(len(h2), len(p), len(date), len(image), len(links))
h2.extend([None] * (max_len - len(h2)))
p.extend([None] * (max_len - len(p)))
date.extend([None] * (max_len - len(date)))
image.extend([None] * (max_len - len(image)))
links.extend([None] * (max_len - len(links)))
detail.extend([None]*(max_len-len(h2)))
# Create DataFrame
# f={'Discription':detail}
d = {'News_Title': h2, 'Short_Discrition': p, 'Date': date, 'Image': image, 'Link': links,'Discription':detail}
bf = pd.DataFrame(d)

# Convert DataFrame to JSON
json_data = bf.to_json(orient='records', indent=4)

# Write JSON data to a file
with open('sports_news.json', 'w') as json_file:
    json_file.write(json_data)

print("Data has been saved to sports_news.json")
