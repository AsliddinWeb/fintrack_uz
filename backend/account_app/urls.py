from django.urls import path

# Jwt auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Local
from .views import RegisterView, LogoutView, AccountImageUpdateView, UserUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # Update
    path('update-image/', AccountImageUpdateView.as_view(), name='account-image-update'),
    path('update-user/', UserUpdateView.as_view(), name='user-update'),

]
