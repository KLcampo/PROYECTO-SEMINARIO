from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UbicacionesSerializers, RestaurantesSerializers
from .models import Ubicaciones, Restaurantes
from django.http import Http404
# Create your views here.

#def listar_Ubicaciones(self, request):
 #   ubicaciones = Ubicaciones.objects.filter(pk=1)

class Restaurantes_APIView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):
        restaurantes = Restaurantes.objects.all()
        serializers = RestaurantesSerializers(restaurantes, many=True)
        return Response(serializers.data)

class Restaurantes_APIView(APIView):
        
    def post(self, request, format=None):
        print(request.data)
        serializer = RestaurantesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



    



        


