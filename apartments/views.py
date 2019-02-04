from django.shortcuts import render

from core.views import BaseFindAPIView

from .search.managers import ApartmentSearchManager, OptionSearchManager
from .serializers import OptionSerializer, ApartmentSerializer


class OptionView(BaseFindAPIView):
    serializer_class = OptionSerializer
    search_manager = OptionSearchManager
    many = False


class ApartmentView(BaseFindAPIView):
    serializer_class = ApartmentSerializer
    search_manager = ApartmentSearchManager


def index(request):
    return render(request, 'apartments/index.html', None)
