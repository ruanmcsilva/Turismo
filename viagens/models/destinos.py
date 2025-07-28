from django.db import models
from .agencia import Agencia
from django.contrib.auth import get_user_model
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

user_model = get_user_model()

class Destinos(models.Model):
    nome = models.CharField(max_length=105)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='viagens_imagens/',blank=True, null=True)
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT, related_name='viagens')
    imagem_ajustada = ImageSpecField(source='imagem', processors=[ResizeToFill(1200, 800)],format='JPEG',
                                           options={'quality': 90})
    imagem_praia1 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem_praia2 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem_praia3 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    

    def __str__(self):
        return self.nome