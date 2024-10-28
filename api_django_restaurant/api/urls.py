from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListCreate.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),
    path('categorias/', views.CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('menus/', views.MenuListCreate.as_view(), name='menu-list'),
    path('menus/<int:pk>/', views.MenuDetail.as_view(), name='menu-detail'),
    path('ordenes/', views.OrdenListCreate.as_view(), name='orden-list'),
    path('ordenes/<int:pk>/', views.OrdenDetail.as_view(), name='orden-detail'),
    path('detalles_orden/', views.DetalleOrdenListCreate.as_view(), name='detalleorden-list'),
    path('detalles_orden/<int:pk>/', views.DetalleOrdenDetail.as_view(), name='detalleorden-detail'),
]
