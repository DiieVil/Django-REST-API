from django.urls import path, include
from rest_framework import routers
from API import views

# El router sirve para manejar todas las rutas de la API
router = routers.DefaultRouter()
router.register(r'programador', views.ProgramadorViewSet)

# Se incluyen las rutas del router, en este caso solo la del programador 
urlpatterns=[
    path('', include(router.urls))
]