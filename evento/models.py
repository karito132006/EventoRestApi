from django.db import models

# Modelo base para eventos generales
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()  # DateField para almacenar fechas
    lugar = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre  # Representación de la instancia del modelo

    class Meta:
        db_table = 'Evento'
        abstract = True  # Esto indica que esta clase no creará una tabla en la base de datos

# Modelo para conciertos que hereda de Evento
class Concierto(Evento):
    artista = models.CharField(max_length=100)
    duracion = models.DurationField()  # DurationField para almacenar la duración

    class Meta:
        db_table = 'Concierto'  # Nombre de la tabla en la base de datos

# Modelo para conferencias que hereda de Evento
class Conferencia(Evento):
    tema = models.CharField(max_length=100)
    orador = models.CharField(max_length=100)

    class Meta:
        db_table = 'Conferencia'  # Nombre de la tabla en la base de datos
