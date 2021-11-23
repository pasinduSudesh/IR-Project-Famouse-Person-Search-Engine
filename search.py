from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import queries

client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'famous-persons'

def search(search_query):
    es_query = queries.multi_match_agg_cross(search_query)

    result = client.search(index=INDEX, body=es_query)

    return result