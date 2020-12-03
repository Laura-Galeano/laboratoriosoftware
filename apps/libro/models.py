from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
#Autor es el usuario
class autor(models.Model):

    ciudad_elecciones=[
        ('Armenia','Armenia'),('Barranquilla','Barranquilla'),('Bello','Bello'),
        ('Bogotá','Bogotá'),('Bucaramanga','Bucaramanga'),('Cali','Cali'),('Cartagena','Cartagena'),
        ('Cúcuta','Cúcuta'),('Ibagué','Ibagué'),('Manizales','Manizales'),
        ('Medellín','Medellín'),('Montería','Montería'),('Neiva','Neiva'),
        ('Cartagena','Cartagena'),('Pasto','Pasto'),('Pereira','Pereira'),
        ('Santa Marta','Santa Marta'),('Soacha','Soacha'),
        ('Soledad','Soledad'),('Valledupar','Valledupar'),('Villavicencio','Villavicencio')
    ]

    orientacion= [
        ('Femenino','Femenino'),
        ('Masculino','Masculino'),
        ('Otro','Otro')
    ]

    temas_elecciones=[
        ('Historia y Geografía', 'Historia y Geografía'),('Narrativa', 'Narrativa'),('Juvenil', 'Juvenil'),('Ciencias físicas', 'Ciencias físicas'),
        ('Infantil', 'Infantil'),('Ciencias Sociales y política', 'Ciencias Sociales y política'),('Medicina y salud', 'Medicina y salud'),
        ('Filosofía', 'Filosofía'),('Arquitectura', 'Arquitectura'),('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'),('Varios', 'Varios'),
    ]

    tipos_autor=[
        ('Cliente','Cliente'),
        ('Administrador','Administrador'),
    ]

    id_autor = models.AutoField(primary_key=True)
    cedula = models.CharField('Cedula', max_length=20, blank=False, null=True, unique=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacimiento = models.DateField('Fecha de nacimiento', blank=False, null=True)
    ciudad = models.CharField('Ciudad de residencia', choices=ciudad_elecciones,max_length= 200,blank=False, null=False, default='1')#, default='1'
    genero = models.CharField('Genero', choices=orientacion, max_length=15, blank=False, null=True)
    email = models.EmailField('Correo Electrónico', max_length=254, unique = True, null=True)
    temas_preferidos = MultiSelectField('Temas de preferencia',choices=temas_elecciones,blank=True, null=True)
    usuario = models.CharField('Nombre de usuario', unique=True, max_length=100, null=True)
    contrasena = models.CharField('Contrasena', max_length=30, null=True, blank=False)
    suscripcion = models.BooleanField('Suscribirme a noticias',blank=True, null=True, default=False)
    tipo_autor = models.CharField('Tipo de usuario', blank=True, null=True, choices=tipos_autor, default='Cliente', max_length=20)
    #nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    #descripcion = models.TextField(blank=False, null=False)
    #fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class libro(models.Model):

    editoriales=[
        ('Norma','Norma'),
        ('Planeta','Planeta'),
        ('Alfaomega','Alfaomega'),
        ('Mundo libro','Mundo libro'),
        ('Penguin','Penguin'),
        ('Kinesis','Kinesis'),
        ('Andina','Andina'),
        ('Deusto','Deusto'),
        ('Maeva','Maeva'),
        ('Ariel','Ariel'),
        ('Critica','Critica'),
        ('Salamandra','Salamandra'),
    ]

    idiomas = [
        ('Espanol','Espanol'),
        ('Ingles','Ingles'),
    ]

    temas_elecciones=[
        ('Historia y Geografía', 'Historia y Geografía'),('Narrativa', 'Narrativa'),('Juvenil', 'Juvenil'),('Ciencias físicas', 'Ciencias físicas'),
        ('Infantil', 'Infantil'),('Ciencias Sociales y política', 'Ciencias Sociales y política'),('Medicina y salud', 'Medicina y salud'),
        ('Filosofía', 'Filosofía'),('Arquitectura', 'Arquitectura'),('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'),('Varios', 'Varios'),
    ]

    issn = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=True)
    autor_id = models.ForeignKey(autor, on_delete=models.CASCADE)
    paginas = models.IntegerField('Paginas', null=True)
    editorial = models.CharField('Editorial', max_length=200, choices=editoriales, default=None)
    idioma = models.CharField('Idioma', max_length=20, choices=idiomas, default='Espanol')
    fecha_publicacion = models.DateField('Fecha publicacion', blank=False, null=False)
    es_nuevo = models.BooleanField('Nuevo', default=True)
    precio = models.IntegerField('Precio del libro', null=True)
    cantidad = models.IntegerField('Cantidad de ejemplares', null=True)
    agotado = models.BooleanField('Agotado', default=False)
    genero = models.CharField('Generos', choices=temas_elecciones, default=None, max_length=50)

    #OneToOneField Esta relacion es de uno a uno, un libro por autor
    #ForeingKey Nos permite que un autor tenga muchos libros, on_delete=models.CASCADE es necesario aqui
    #ManyToMany permite que se puedan seleccionar varios autores por los libro
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo

class tarjeta(models.Model):
    tipos_tarjetas=[
        ('Debito','Debito'),
        ('Credito','Credito'),
    ]

    id_tarjeta = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la tarjeta', max_length=30, null=True)
    caducidad = models.DateField('Fecha de caducidad', blank=False, null=True)
    tipo_tarjeta = models.CharField('Tipo de tarjeta', default='Credito', max_length=30, choices=tipos_tarjetas)
    saldo = models.IntegerField('Saldo', null=True)
    id_autor = models.ForeignKey(autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'

    def __str__(self):
        return self.nombre

class carrito(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_autor = models.CharField('ID autor', max_length=30, null=True)
    issn = models.CharField('ISSN', max_length=30, null=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.id_autor
