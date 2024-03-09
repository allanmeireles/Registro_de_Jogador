from rest_framework.decorators import api_view
from app.models import playerRegister
from app.serializers import playerSerializer
from rest_framework import response
from rest_framework import status

#manipula os registros de jogadores 
@api_view(['GET','POST'])
def playerRegister(request):
    if request.method == 'GET':
        list = playerRegister.objects.all()
        serializer = playerSerializer(playerRegister, many=True)
        return response(serializer.data)
    elif request.method == 'POST':
        serializer = playerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREARTED)
        return response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
#Modifica e exclui    
@api_view(['GET','PUT','DELETE'])
def playerRegister_change_and_delete(request, pk):
    try: 
        playerRegister.objects.get(pk=pk)
    except playerRegister.DoesNotExist:
         return response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer = playerSerializer(playerRegister)
        return response(serializer.data)
    elif request.method == 'PUT':
        serializer = playerSerializer(playerRegister, data = request.data)
        if serializer.is_valid():
            return response(playerSerializer.data)
        return response(serializer.erros, status=status.HTTP_204_NO_CONTENT)
     

