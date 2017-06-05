# indexing python file created 05/06/2017 by fshaw

__author__ = 'felixshaw'
import pymongo
from bson import ObjectId
from settings import NOUNS
from django.conf import settings


def get_collection_ref(collection_name):
    return settings.MONGO_CLIENT[collection_name]


def to_mongo_id(id):
    return ObjectId(id)


def cursor_to_list(cursor):
    records = []
    for r in cursor:
        try:
            r['id'] = r.pop('_id')
        except:
            pass
        records.append(r)
    return records


keywordsReference = 'keywordsCollection'

handle_dict = dict(
    keywords=get_collection_ref(keywordsReference)
)


def get_collection_handle(component):
    return handle_dict.get(component)


def save_keyword_set(keyword_set):
    pass



