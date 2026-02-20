from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin can see all tasks
        if user.is_staff:
            return Task.objects.all().order_by('-id')

        # Normal user sees only own tasks
        return Task.objects.filter(created_by=user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
