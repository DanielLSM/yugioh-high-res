database_endpoint = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'


def get_webpage_json(str: url):
    from urllib.request import Request, urlopen
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage
