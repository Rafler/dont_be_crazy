import requests
from bs4 import BeautifulSoup as bs
from api.models import Category, Event

base_url = 'https://afisha.lviv.ua/events'

def get_count_pages(url):
  response = requests.get(url)
  soup = bs(response.content, "html.parser")

  pages = []

  for li in soup.findAll("ul", class_="pagination"):
    for a in li.findAll("li"):
      try:
        pages.append(int(a.text))
      except ValueError:
        pass

  print(pages)
  return len(pages)

def parse_links(url):
  response = requests.get(url)
  soup = bs(response.content, "html.parser")
  
  a = soup.findAll('a', href=True, itemprop="url")
  events = []

  for i in range(len(a)):
    link = 'https://afisha.lviv.ua' + soup.findAll('a', href=True, itemprop="url")[i]['href']
    events.append(link)

  return events

def get_name(soup):

  return {'name': soup.find('h1', itemprop='name').text}

def get_address(soup):
  address = soup.find('div', itemprop='address').text

  return {'address': address}

def get_date_and_time(soup):

  date = soup.find('time', itemprop='startDate')['datetime']

  try:
    time = soup.find('div', 'icon-bg hours').text
  except AttributeError:
    time = ''

  date_and_time = date + " " + time
  return {'date': date_and_time}

def get_description(soup):
  description = soup.find('div', itemprop='description').text
  return {'description': description}

def get_price(soup):
  price = soup.find('div', 'icon-bg price')
  return {'price': price.text}

def get_category(soup):
  category = soup.find('div', 'field-type margin-bottom-xs text-uppercase')
  category = category.find('a').text
  return {"category": category}

def get_photo_url(soup):
  return {'image': soup.find('img', itemprop='image')['src']}

def full_parser(url):
  count_page = get_count_pages(url)

  events = []


  for i in range(count_page):
    event = {}
    if i > 0:
      url = url+'?page='+str(i)

    for link in parse_links(url):
      print(link)
      response = requests.get(link)
      soup = bs(response.content, "html.parser")
      event['name'] = get_name(soup)['name']
      event['image'] = get_photo_url(soup)['image']
      event['category'] = get_category(soup)['category']
      event['date'] = get_date_and_time(soup)['date']
      event['address'] = get_address(soup)['address']
      event['link'] = link
      try:
        event['price'] = get_price(soup)['price']
      except AttributeError:
        event['price'] = "Havem't information"

      event['description'] = get_description(soup)['description']

      events.append(event)

  return events

posts = full_parser(base_url)
print(posts)
def add_post_to_db(posts):
    category_q = Category.objects.values('name')
    categories = []
    for item in category_q:
        categories.append(item['name'])
    for post in posts:
        if post["category"].__contains__("Мистецтво") or post["category"].__contains__("Театр") or post["category"].__contains__("Література"):
            post["category"] = "Виставки"
        elif post["category"] == "Музика":
            post["category"] = "Концерти"
        elif post["category"] == "Бізнес":
            post["category"] = "Конференції"

        elif post["category"].__contains__("Фестивалі"):
            post["category"] = "Фестивалі"

        elif post["category"] not in categories:
            post["category"] = "Інше"

        if not post["price"]:
            post["price"] = "Безкоштовно"
        e = Event.objects.create(
            name=post["name"],
            image=post["image"],
            category=Category.objects.filter(name=post["category"])[0],
            date=post["date"],
            address=post["address"],
            price=post["price"],
            description=post["description"],
            link=post["link"]
        )
add_post_to_db(posts)