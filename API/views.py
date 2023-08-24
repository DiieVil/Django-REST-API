from rest_framework import viewsets
from .serializer import ProgramadorSerializer
from .models import Programador

# Clase necesaria para poder interactuar con la API con el modelo de Programador
class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer