from django.urls import path
from .views import ProfileDetail, UserRegister, CustomLogout, CustomLogin, ProfileEdit

urlpatterns = [
    path('registration/', UserRegister.as_view(), name='registration'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', CustomLogout.as_view(), name='logout'),
    path('profile/<int:profile_pk>/update/', ProfileEdit.as_view(), name='profile_edit'),
    path('profile/<int:profile_pk>/', ProfileDetail.as_view(), name='profile_detail'),
]