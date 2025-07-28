from django.db import models
from django.contrib.auth import get_user_model
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

user_model = get_user_model()

class Pousada (models.Model):
    nome_pousada = models.CharField(max_length=35)
    descricao_pousada = models.TextField()
    preco_pousada = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_pousada = models.ImageField(upload_to='viagens_imagens/',blank=True, null=True)
    imagem_padrao = ImageSpecField(source='imagem_pousada', processors=[ResizeToFill(1200, 800)],format='JPEG',
                                        options={'quality': 90})
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_pousada