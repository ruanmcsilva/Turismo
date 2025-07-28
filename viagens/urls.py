from django.urls import path
from .views import viagens_list,viagens_description,passeio_list,ecologica_list,pousada_description, carros_list, carros_description,contato_description,passeios_description

app_name = 'viagens'

urlpatterns = [
    path('',viagens_list, name='list_viagens'),
    path('<int:pk>/', viagens_description, name='description_viagens'),
    path('passeios/',passeio_list , name='list_passeio'),
    path('rotaecologica/', ecologica_list, name='list_ecologica'),
    path('pousadas/',pousada_description, name='description_pousada'),
    path('veiculo/', carros_list, name='list_carros'),
    path('descricaocarro/<int:pk>/', carros_description, name='description_carros'), # adicionei aqui, o nome da pagina da nova pagina do html
    path('contato/',contato_description, name = 'description_contato'),
    path('descricaopasseio/<int:pk>/', passeios_description, name='description_passeios'),
]