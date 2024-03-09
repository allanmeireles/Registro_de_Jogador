from app.models import playerRegister
from rest_framework import serializers

#Converte o modelo playerRegister em representações JSON
class playerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = playerRegister
        fields = ['idade','time','jersey_number', 'nacionalidade', 'posição']
