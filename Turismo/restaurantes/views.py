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
    
class Restaurantes_APIView_Detail(APIView):

    def get_object(self, pk):
        try: 
            return Restaurantes.objects.get(pk=pk)
        except Restaurantes.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        restaurante = self.get_object(pk)
        serializer = RestaurantesSerializers(restaurante)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        restaurante = self.get_object(pk)
        serializer = RestaurantesSerializers(restaurante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        restaurante = self.get_object(pk)
        restaurante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Ubicaciones_APIView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):
        ubicacion = Ubicaciones.objects.all()
        serializers = UbicacionesSerializers(ubicacion, many=True)
        return Response(serializers.data)

class Ubicaciones_APIView(APIView):
        
    def post(self, request, format=None):
        print(request.data)
        serializer = UbicacionesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Ubicaciones_APIView_Detail(APIView):

    def get_object(self, pk):
        try: 
            return Ubicaciones.objects.get(pk=pk)
        except Ubicaciones.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        ubicacion = self.get_object(pk)
        serializer = UbicacionesSerializers(ubicacion)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        ubicacion = self.get_object(pk)
        serializer = UbicacionesSerializers(ubicacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        ubicacion = self.get_object(pk)
        ubicacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    



        


