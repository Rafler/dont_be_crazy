import requests
from bs4 import BeautifulSoup as bs
import os
from api.models import Event, Category
import time
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

base_url = 'https://www.zankovetska.com.ua/playbill/http:/www.zankovetska.com.ua/playbill/'


def get_links(base_url, headers):
    links = []
    bd_qeury_links = Event.objects.values('link')
    bd_links = []
    link_to_parse = []
    for item in bd_qeury_links:
        bd_links.append(item["link"])
    
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    
    soup = bs(request.content, 'html.parser')
    content = soup.find('div', attrs={'id': 'content'})
    left_content = content.find('div', attrs={'class': 'left_content'})
    main_content = left_content.find('div')
    divs = main_content.find_all('div', attrs={'class': 'playbill_block'})
    # print(divs)
    for div in divs:

        vystava = div.find('div', attrs={'class': 'playbill_vystava'})
        block = vystava.find('div', attrs={'class': 'info_block'})    
        
        if block:
            td = block.find('td', attrs={'class': 'info'})
            # print(td)
            
            link = "https://www.zankovetska.com.ua" + td.find('a')['href']
            if link not in bd_links:
                link_to_parse.append(link)
    return link_to_parse

links = get_links(base_url, headers)


def parse_posts(links,headers):
    posts = []
    session = requests.Session()
    
    for page in links:
        request = session.get(page, headers=headers)
        soup = bs(request.content, 'html.parser')        
        name = soup.find('h1', attrs={'itemprop': 'name'})
        description = soup.find('div', attrs={'class': 'performance_text'}).text
        address = "Театр ім. Марії Занковецької"
        date = soup.find('div', attrs={'class':'vdates'})
        category = "Театр"
        price = "На касі"
        image = "https://www.zankovetska.com.ua"+str(soup.find('img', attrs={'itemprop': 'image'})['src'])
        
        if date:
            date = date.find('span').text
        else:
            date = "Скоро"
        post = {
            'name':name,
            'description': description,
            'address': address,
            'date': date,
            'category': category,
            'price': price,
            'image': image,
            'link': page
        }
        posts.append(post)
    return posts   
posts = parse_posts(links,headers)
def add_post_to_db(posts):
    category_q = Category.objects.values('name')
    categories = []
    for item in category_q:
        categories.append(item['name'])
    for post in posts:
        
        
        e = Event()
        e.name=post["name"],
        e.image=post["image"],
        e.category=Category.objects.get(id=1),
        e.date=post["date"],
        e.address=post["address"],
        e.price=post["price"],
        e.description=post["description"],
        e.link = post["link"]
        e.save()
        print(e)

print(posts)
add_post_to_db(posts)
