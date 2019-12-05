from rest_framework.views import APIView
from rest_framework.response import Response


class BaseView(APIView):
    authentication_classes = ()
    permission_classes = ()
    @staticmethod
    def get(request):
        return Response({
            'message': 'Welcome to Cowry Beta!'
        })