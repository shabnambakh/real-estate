from django.core.management.base import BaseCommand

from ...search_index import open_index


class Command(BaseCommand):
    def handle(self, *args, **options):
        open_index()
