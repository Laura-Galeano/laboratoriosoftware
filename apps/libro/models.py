from django.db import models

# Create your models here.

class autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha publicacion', blank=False, null=False)
    autor_id = models.ForeignKey(autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)



    #OneToOneField Esta relacion es de uno a uno, un libro por autor
    #ForeingKey Nos permite que un autor tenga muchos libros, on_delete=models.CASCADE es necesario aqui
    #ManyToMany permite que se puedan seleccionar varios autores por los libro



    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
