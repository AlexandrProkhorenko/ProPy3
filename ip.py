import requests
import bs4

response = requests.get('https://habr.com/ru/all/')
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Удалённая работа']
KEYWORDS_set = set(KEYWORDS)
if response.status_code == 200:
    print('Успешное подключение!')
    print('Начинаю парсить...')


    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all(class_='tm-article-snippet__hubs-item')
        hubs = set(hub.find('span').text for hub in hubs)
        if KEYWORDS_set & hubs:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = "https://habr.com" + href
            date = article.find(class_='tm-article-snippet__datetime-published')
            print(date.text, '-', article.find('h2').text, '-', link)

else:
    print('Не удалось подключится!')










