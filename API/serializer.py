from rest_framework import serializers
from .models import Programador

class ProgramadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Programador
        # fields = ('fullname','nickname','age','is_active') o bien como en la siguiente linea, que tiene en cuenta todos los campos más el ID
        fields = '__all__'