from django.conf import settings
from elasticsearch import Elasticsearch


class ElasticsearchDriverException(BaseException):
    pass


class ElasticsearchDriver:

    def __init__(self):
        self.connection = Elasticsearch(
            [f"http://{settings.ES_HOST}:{settings.ES_PORT}"],
            http_auth=(settings.ES_USER, settings.ES_PASSWORD)
        )
        if not self.connection.ping(http_auth=(settings.ES_USER, settings.ES_PASSWORD)):
            raise ElasticsearchDriverException(f"Unable to connect to the specified address "
                                               f"({settings.ES_HOST}:{settings.ES_PORT})")

    def store_record(self, index_name: str, record_id: str, record):
        try:
            return self.connection.index(index=index_name, id=record_id, document=record)
        except Exception as ex:
            raise ElasticsearchDriverException(f'Error while indexing data: {str(ex)}')

    def get_record(self, index_name: str, record_id: str):
        try:
            return self.connection.get(index=index_name, id=record_id)
        except Exception as ex:
            raise ElasticsearchDriverException(f'Error while getting data: {str(ex)}')

    def refresh_index(self, index_name: str):
        try:
            return self.connection.indices.refresh(index=index_name)
        except Exception as ex:
            raise ElasticsearchDriverException(f'Error while refreshing index: {str(ex)}')

    def search(self, index_name: str, query: str = '*'):
        query = {
            "query_string": {
                "fields": ["*"],
                "query": query
            }
        }
        try:
            return self.connection.search(index=index_name, query=query)
        except Exception as ex:
            raise ElasticsearchDriverException(f'Error while refreshing index: {str(ex)}')
