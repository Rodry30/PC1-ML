from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('predict/', views.api_predict, name='api_predict'),
]