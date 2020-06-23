from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    """Test Api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of api view"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'is similar to a traditional Django view'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})


    def post(self, request):
        """Create  a helllo message with our name"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
             )


    def put(self, request, pk=None):
        """Handle updating an obj"""
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """ Handle a partial update of an object"""
        return Response({'method': 'PATCH'})


    def delete(self , request , pk=None):
        """ Deleteing object"""
        return Response({'method':'DELETE'})
