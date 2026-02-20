from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Sirf logged-in user ke tasks dikhaye
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Task create hote waqt user automatically set hoga
        serializer.save(created_by=self.request.user)
