from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  todo.api.serializer import TodoSerializer
from .models import Todo

@api_view(['GET']) 
def List(request) :
    person =Todo.objects.all()
    serializer =TodoSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST']) 
def Create(request) :
    serializer =TodoSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data)

@api_view(["PUT"]) 
def Update(request, pk) :
    person =get_object_or_404(Todo, id =pk)
    serializer =TodoSerializer(instance=person, data =request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data)

@api_view(["GET"])
def Detail(request, pk) :
    person =get_object_or_404(Todo, id =pk)
    serializer =TodoSerializer(person)
    return Response(serializer.data)

@api_view(['DELETE'])
def Delete(request, pk) :
    person =get_object_or_404(Todo, id=pk)
    person.delete()
    return Response(status =status.HTTP_204_NO_CONTENT)
