from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from .models import Task
# Module docstring: Task management API views

class RegisterView(APIView):
    """
    Handles user registration.
    """

    def post(self, request):
        """
        Registers a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(APIView):
    """
    API view to retrieve a list of tasks or create a new task.
    """
    permission_classes = [IsAuthenticated] # Ensures only authenticated users can access

    def get(self, request):
        """
        Handles GET requests to list all tasks for the authenticated user.
        """
        # pylint: disable=no-member
        tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handles POST requests to create a new task for the authenticated user.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save the task with the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    """
    API view to retrieve, update, or delete a specific task.
    """
    permission_classes = [IsAuthenticated] # Ensures only authenticated users can access
    
    def get(self, request, pk):
        """
        Handles GET requests to retrieve a specific task by its ID.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure the task belongs to the authenticated user
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Handles PUT requests to update a specific task by its ID.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure the task belongs to the authenticated user
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handles DELETE requests to delete a specific task by its ID.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)  # Ensure the task belongs to the authenticated user
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
