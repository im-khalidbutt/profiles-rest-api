from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):
     """ Test API VIewSet"""
     serializer_class = serializers.HelloSerializer


     def list(self, request):
         """ Return Hello message"""

         a_viewset = [
            'Uses actions (List, reterive, update, destroy, partial_upadate)',
            'automatically maps to urls using router',
            'provides more functionality with less code',

         ]
         return Response({'message': 'hello', 'a_viewset': a_viewset})

     def create(self, request):
         """Create a new hello message"""
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

     def retrieve(self, request, pk=None):
         """ Handle Getting an object by its ID"""
         return Response({'http_method': 'GET'})

     def update(self, request, pk=None):
         """Handle updatinfgobject"""
         return Response({'http_method': 'PUT'})

     def partial_update(self, request, pk=None):
         """Handle updating part of an object"""
         return Response({'http_method': 'PATCH'})

     def destroy(self, request, pk=None):
         """Handle Removing an object"""
         return Response({'http_method': 'DELETE'})
