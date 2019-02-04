from core.views import BaseGenericAPIView

from .models import City
from .serializers import CitySerializer


class CityView(BaseGenericAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
