from rest_framework import serializers
from .models import Flores, Arboles

class FloresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flores
        fields='__all__'
        
class ArbolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Arboles
        fields='__all__'