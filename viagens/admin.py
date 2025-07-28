from django.contrib import admin
from .models.destinos import Destinos
from .models.agencia import Agencia
from .models.passeio import Passeio
from .models.ecologica import Ecologica
from .models.pousada import Pousada
from .models.carros import Aluguel
from.models.negociar import (Negociar)
# Register your models here.

admin.site.register(Destinos)
admin.site.register(Agencia)
admin.site.register(Passeio)
admin.site.register(Ecologica)
admin.site.register(Pousada)
admin.site.register(Aluguel)
admin.site.register(Negociar)