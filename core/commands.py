from django.core.management.base import BaseCommand


class BaseAppCommand(BaseCommand):
    default_size = 10
    factory_model = None

    def add_arguments(self, parser):
        parser.add_argument('--size', type=int, dest='size', required=False)

    def handle(self, *args, **options):
        size = options.get('size')
        if not size:
            size = self.default_size

        assert self.factory_model is not None, (
                "'%s' should either include a `factory_model` attribute."
                % self.__class__.__name__
        )

        self.factory_model.create_batch(size=size)
