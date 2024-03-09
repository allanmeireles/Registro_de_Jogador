from app.models import playerRegister
from rest_framework import serializers

class playerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = playerRegister
        fields = ['idade','time','jersey_number', 'nacionalidade', 'posição']
        