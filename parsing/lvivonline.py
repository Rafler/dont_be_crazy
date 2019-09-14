import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

base_url = 'https://lviv-online.com/ua/events/'

def parse_count_pages(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            pagination = soup.find('div', attrs={'class': 'page_navigation'})
            pagination_items = pagination.find('a')
            return len(pagination_items) + 1

def parse_links(base_url, headers):
    links = []
    count_pages = parse_count_pages(base_url, headers)
    for i in range(1,count_pages+1):
        session = requests.Session()
        request = session.get(base_url+"page/"+str(i)+"/", headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            events = soup.find_all('div', attrs={'class':'events--list__category'})[0]
            articles = events.find_all('article')
            for article in articles:
                link = article.find('a', attrs={'itemprop':'url'})['href']
                links.append(link)
    return links

def parse_posts(pages, headers):
    session = requests.Session()
    posts = []
    for page in pages:
        session = requests.Session()
        request = session.get(page, headers=headers)
        soup = bs(request.content, 'html.parser')
        main_content = soup.find('div', attrs={'id':'page--content'})
        # find category
        category_wrapper = main_content.find('div', attrs={'class': 'sitemap--category'})
        
        
        # find name
        article = main_content.find('article', attrs={'class': 'single--event'})
        article_preview = article.find('header', attrs={'class': 'single--event--preview'})
        article_preview_inforamtion = article_preview.find('div', attrs={'class': 'single--event--preview--iformation'})
        # article_preview_details = article_preview.find('div', attrs={single--event--details})
        
        category = category_wrapper.find('a', attrs={'rel': 'category tag'}).text
        image = article_preview_inforamtion.find('img', attrs={'class': 'single--event--poster'})['src']
        name = article_preview.find('h1',attrs={'class': 'single--event--title'}).text[1:]
        # parse date
        date = article_preview.find('p', attrs={'class':'single--event--time'}).text.replace("\n", "")
        
        # parse address
        address_p = article_preview.find('div', attrs={'class': 'single--event--place'})
        address = address_p.find('span', attrs={'itemprop': 'name'}).text
        address = address.replace('\n','')
        
        # parse price
        price = main_content.find('p', attrs={'class': 'single--event--tickets__price'})
        if price:
            price = price.text

        # parse description

        description_div = main_content.find('div', attrs={'class': 'single--event--text'})
        description_p = description_div.find_all('p')
        description = ""
        for p in description_p:
            if p.text:
                description+=p.text
        
        post = {
            'name': name,
            'image': image,
            'category': category,
            'date': date,
            'address': address,
            'price': price,
            'description': description

        }
        posts.append(post)
    return posts
links = parse_links(base_url, headers)
posts = parse_posts(links, headers)
print(posts)
