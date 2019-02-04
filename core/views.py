from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class BaseGenericAPIView(GenericAPIView):
    def get(self, request):
        return Response({
            'results': self.get_serializer(self.get_queryset(), many=True).data
        })


class BaseFindAPIView(GenericAPIView):
    search_manager = None
    many = True

    def get(self, request):
        assert self.search_manager is not None, f'"{self.__class__.__name__}" should set a \'search_manager\' attribute'

        results = self.search_manager().do_search(request.query_params)

        return Response({
            'results': self.get_serializer(results, many=self.many).data
        })