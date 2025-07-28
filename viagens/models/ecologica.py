from django.db import models
from django.contrib.auth import get_user_model
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

user_model = get_user_model()

class Ecologica(models.Model):

    nome_rota = models.CharField(max_length=55)
    descricao_rota = models.TextField(blank=True, null=True)
    imagem_rota = models.ImageField(upload_to='viagens_imagens/',blank=True,null=True)
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)
    imagem_ajustada = ImageSpecField(source='imagem_rota', processors=[ResizeToFill(1200, 800)],format='JPEG',
                                           options={'quality': 90})
    def __str__(self):
        return self.nome_rota