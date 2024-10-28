# Create your views here.
from rest_framework import generics
from .models import Cliente, Categoria, Menu, Orden, DetalleOrden
from .serializers import ClienteSerializer, CategoriaSerializer, MenuSerializer, OrdenSerializer, DetalleOrdenSerializer

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrdenListCreate(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class DetalleOrdenListCreate(generics.ListCreateAPIView):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer

class DetalleOrdenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer
