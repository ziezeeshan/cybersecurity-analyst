import json
from elasticsearch import Elasticsearch

es = Elasticsearch()

def ingest(path):
    with open(path) as f:
        data = json.load(f)
    for obj in data.get('objects', []):
        es.index(index='stix', id=obj.get('id'), document=obj)

if __name__ == '__main__':
    ingest('feeds/enterprise-attack.json')
    print('[+] Feeds ingested.')
