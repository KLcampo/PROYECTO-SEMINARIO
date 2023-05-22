from django.urls import path
from .views import Restaurantes_APIView, Restaurantes_APIView_List, Restaurantes_APIView_Detail, Ubicaciones_APIView, Ubicaciones_APIView_List, Ubicaciones_APIView_Detail

urlpatterns = [
    path('v1/rest/add', Restaurantes_APIView.as_view()),
    path('v1/rest', Restaurantes_APIView_List.as_view()),
    path('v1/rest/<int:pk>', Restaurantes_APIView_Detail.as_view()),
    path('v1/ubi/add', Ubicaciones_APIView.as_view()),
    path('v1/ubi', Ubicaciones_APIView_List.as_view()),
    path('v1/ubi/<int:pk>', Ubicaciones_APIView_Detail.as_view())


]
