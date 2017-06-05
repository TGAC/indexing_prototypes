# indexing python file created 02/06/2017 by fshaw

import requests
from requests.compat import urljoin
import json


figshare_base = 'https://api.figshare.com/v2/'


def figshare_get_articles():

    method = 'articles'
    resp = requests.get(get_url(method))
    answer = json.loads(resp.content.decode('utf-8'))

    return resp

def figshare_get_article(a_id):

    method = 'articles' + '/' + a_id
    resp = requests.get(get_url(method))
    answer = json.loads(resp.content.decode('utf-8'))

    return resp

def figshare_search_general(search_term):
    method = 'articles/search'
    url = get_url(method)
    json = {'search_for': search_term}
    resp = requests.post(url, json=json)

    return resp


def get_url(method):
    return urljoin(figshare_base, method)