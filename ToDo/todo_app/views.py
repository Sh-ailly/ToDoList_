from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import todomodel
from .serializers import TodoSerializer
#Create your view here
class TodoList(APIView):

    # List all todos
    def list(self, request):
        todos = todomodel.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    # Retrieve a single todo or list all if no pk is provided
    def get(self, request, pk=None):
        if pk:
            todo = get_object_or_404(todomodel, pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        else:
            return self.list(request)

    # Create a new todo
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Full update of a todo item
    def put(self, request, pk):
        todo = get_object_or_404(todomodel, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH updates only specified fields
    def patch(self, request, pk):
        todo = get_object_or_404(todomodel, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a todo item
    def delete(self, request, pk):
        todo = get_object_or_404(todomodel, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
