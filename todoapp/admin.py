from django.contrib import admin

# Register your models here.
from todoapp.models import Categoria, User, Tarea
from categorias.models import Categoria

admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Tarea)