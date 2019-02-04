from django.conf import settings
from django.apps import AppConfig

from elasticsearch_dsl.connections import connections


class SearchConfig(AppConfig):
    name = 'search'

    def ready(self):
        super().ready()

        if settings.ELASTICSEARCH_HOST:
            self._create_default_connection()

    @staticmethod
    def _create_default_connection():
        connections.create_connection(
            hosts=[settings.ELASTICSEARCH_HOST],
            timeout=30
        )
