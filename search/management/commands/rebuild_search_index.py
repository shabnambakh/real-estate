from django.core.management.base import BaseCommand

from ...search_index import rebuild_index


class Command(BaseCommand):
    def handle(self, *args, **options):
        rebuild_index()
