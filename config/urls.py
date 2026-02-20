from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Register API
    path('api/v1/', include('accounts.urls')),

    # Login API (JWT)
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login'),

    # Refresh Token API
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/', include('tasks.urls')),

    # Swagger schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


]
