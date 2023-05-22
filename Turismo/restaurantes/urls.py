from django.urls import path
from .views import Restaurantes_APIView, Restaurantes_APIView_List

urlpatterns = [
    path('v1/rest/add', Restaurantes_APIView.as_view()),
    path('v1/rest', Restaurantes_APIView_List.as_view())
]
