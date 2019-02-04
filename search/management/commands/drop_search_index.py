from django.core.management.base import BaseCommand

from ...search_index import drop_index


class Command(BaseCommand):
    def handle(self, *args, **options):
        drop_index()
