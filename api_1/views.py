from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from api_1.models import TodoLists
from api_1.serializers1 import TodoListSerializer
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status
# Create your views here.


class api(generics.ListCreateAPIView):
    queryset = TodoLists.objects.all()
    serializer_class = TodoListSerializer


class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoLists.objects.all()
    serializer_class = TodoListSerializer


@api_view(['POST'])
def createTodo(request):
    item = TodoListSerializer(data=request.data)
    if TodoLists.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Todolist is already")
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update(request, pk):
    item = TodoLists.objects.get(pk=pk)
    data = TodoListSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete(request, pk):
    item = get_object_or_404(TodoLists, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
