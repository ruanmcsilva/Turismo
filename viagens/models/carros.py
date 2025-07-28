from django.db import models
from django.contrib.auth import get_user_model
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField


user_model = get_user_model()

class Aluguel(models.Model):
    
    nome_carro = models.CharField(max_length=20)
    descricao_veiculo = models.TextField(null=True)
    imagem = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem_ajustada = ImageSpecField(source='imagem', processors=[ResizeToFill(300, 200)],format='JPEG',
                                           options={'quality': 90})
    imagem1 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='viagens_image/', blank=True, null=True)
    def __str__(self):
        return self.nome_carro