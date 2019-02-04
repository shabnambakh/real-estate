from django.core.management.base import BaseCommand

from ...search_index import update_index_mapping, update_index_settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_index_mapping()
        update_index_settings()
