from django.db import models

class clientes(models.Model):
    identificacion_cliente = models.CharField(max_length=20, unique=True, primary_key=True)  # Clave primaria
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class mascotas(models.Model):
    codigo_mascotas = models.AutoField(unique= True, primary_key=True)  # Clave primaria
    identificacion_cliente = models.ForeignKey(clientes, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    alimentacion = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True)
    genero = models.CharField(max_length=1, choices=[('M', 'Macho'), ('F', 'Hembra')], null=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.nombre

class empleados(models.Model):
    codigo_empleado = models.CharField(unique=True,primary_key=True, max_length=200)  # Clave primaria
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=100, null=True)
    codigo_cargo = models.ForeignKey('cargos', on_delete=models.CASCADE, related_name='empleados', null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class cargos(models.Model):
    codigo_cargo = models.CharField(primary_key=True, max_length=200, unique=True)  # Clave primaria
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo_cargo ,self.descripcion}"

class citas(models.Model):
    codigo_cita = models.CharField(primary_key=True, max_length=200, unique=True)  # Clave primaria
    codigo_empleado = models.ForeignKey(empleados, on_delete=models.CASCADE, related_name='citas', null=True)
    codigo_mascotas = models.ForeignKey(mascotas, on_delete=models.CASCADE, related_name='citas', null=True)
    fecha = models.DateTimeField()
    codigo_servicio = models.ForeignKey('servicios', on_delete=models.CASCADE, related_name='citas', null=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Cita para {self.codigo_mascotas.nombre} el {self.fecha}"

class servicios(models.Model):
    codigo_servicio = models.AutoField(primary_key=True, unique=True)  # Clave primaria
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
