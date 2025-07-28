from django.db import models
from .agencia import Agencia
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

from django.contrib.auth import get_user_model

user_model = get_user_model()

class Passeio(models.Model):
    titulo_passeio = models.CharField(max_length=200)
    descricao_passeio = models.TextField()
    cronograma_passeio = models.TextField()
    imagem_passeio = models.ImageField(upload_to='viagens_imagens/',blank=True,null=True)
    imagem_reformulada = ImageSpecField(source='imagem_passeio', processors=[ResizeToFill(300, 200)],format='JPEG',
                                           options={'quality': 90})
    imagem_passeio1 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem_passeio2 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem_passeio3 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo_passeio