from django.urls import path

from common.views import CityView

from .views import index, ApartmentView, OptionView


urlpatterns = [
    path('', index, name='index'),
    path(r'api/cities/', CityView.as_view()),
    path(r'api/apartments/', ApartmentView.as_view()),
    path(r'api/options/', OptionView.as_view())
]
