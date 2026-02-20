from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from .serializers import RegisterSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]
