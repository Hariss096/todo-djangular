#docstring

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset =Todo.objects.all()
    serializer_class = TodoSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
 
    def get_queryset(self):
      return Todo.objects.all().filter(user=self.request.user)
