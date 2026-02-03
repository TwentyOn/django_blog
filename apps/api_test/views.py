from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet
from rest_framework.decorators import action
from django.db.models import Count, Sum
from django.db.models import DecimalField, IntegerField

from .models import Book, Order
from .serializers import BookSerializer


# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        items = Book.objects.all()
        serializer = BookSerializer(instance=items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class Test(GenericAPIView):
    queryset = Book.objects.all()
    # lookup_field = 'pk'
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        print(self.get_serializer(), type(self.get_serializer()))
        print(self.get_serializer_class(), type(self.get_serializer_class()))
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


class Test2(GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    # Напишите ваше решение сюда.
    @action(detail=True, methods=['get'])
    def stats(self, request, *args, **kwargs):
        print(request.user)
        items = Order.objects.filter(
            user=request.user).aggregate(total_orders=Count('id'),
                                         total_amount=Sum('total_amount'))
        return Response(dict(items))
