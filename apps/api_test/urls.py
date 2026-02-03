from django.urls import path
from rest_framework import routers
from .views import books, Test, Test2

router = routers.DefaultRouter()
router.register('books', Test2)

urlpatterns = router.urls