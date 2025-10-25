from django.urls import path
from .views import ProfileDetail, UserRegister, CustomLogout, CustomLogin

urlpatterns = [
    path('create_user/', UserRegister.as_view(), name='register_user'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', CustomLogout.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]