import urllib.request, json
from .models import News, Headlines

# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting news secondary url
secondary_url = None


def configure_request(app):
    global api_key, base_url, secondary_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    secondary_url = app.config['NEWS_API_SECONDARY_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        url = news_item.get('url')
        category = news_item.get('category')

        if name:
            news_object = News(id, name, url, category)
            news_results.append(news_object)

    return news_results


def get_headlines(id):
    get_headlines_url = secondary_url.format(id, api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)

    return headlines_results


def process_headlines(headlines_list):
    headlines_results = []
    for headlines_items in headlines_list:
        id = headlines_items.get('id')
        title = headlines_items.get('title')
        description = headlines_items.get('description')
        url = headlines_items.get('url')
        urlToImage = headlines_items.get('urlToImage')
        publishedAt = headlines_items.get('publishedAt')

        if title:
            headlines_object = Headlines(
                id, title, description, url, urlToImage, publishedAt)
            headlines_results.append(headlines_object)

    return headlines_results