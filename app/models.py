class News:
    '''
    News class to define News sources Objects
    '''

    def __init__(self, id, name, url, category):
        self.id = id
        self.name = name
        self.url = url
        self.category = category


class Headlines:
    '''
    Headlines to define News Headline class
    '''

    def __init__(self, id, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt