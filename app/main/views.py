from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_headlines
from ..models import News, Headlines


@main.route('/')
def index():
    """ 
    View root page function that returns the index page and its data 
    """
    business_news = get_news('business')
    entertainment_news = get_news('entertainement')
    general_news = get_news('general')
    health_news = get_news('politics')
    science_news = get_news('science')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    title = 'Home - News Sources'
    return render_template('index.html', 
                            title=title,
                            business=business_news,
                            entertainment=entertainment_news, 
                            general=general_news, 
                            health=health_news, 
                            science=science_news, 
                            sports=sports_news, 
                            technology=technology_news,)

@main.route('/headlines/<id>')
def headlines(id):
    """  
    View headlinse from a specific source
    """
    headlines = get_headlines(id)
    title = f'{id}'
    return render_template('news.html',
                           title=title,
                           headlines=headlines
                           )