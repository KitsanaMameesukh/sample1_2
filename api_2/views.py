from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from api_2.models import Emails
from api_2.serializers2 import EmailSerializer
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status
# Create your views here.


class api(generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailSerializer


class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailSerializer


@api_view(['POST'])
def create(request):
    item = EmailSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def reply(request, pk):
    item = Emails.objects.get(pk=pk)
    data = EmailSerializer(instance=item, data=request.data, partial=True)
    if data.is_valid():
        data.save()

    return Response(data.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request, pk):
    item = get_object_or_404(Emails, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
