from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')])

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('preparación', 'Preparación'), ('enviado', 'Enviado'), ('entregado', 'Entregado')])
    usuario_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class DetalleOrden(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    orden_id = models.ForeignKey(Orden, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

