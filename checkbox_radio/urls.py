from django.urls import path
from . import views


urlpatterns = [
    path('', views.mostrar_posts, name='mostrar_posts'),
    path('post/<int:id>', views.post, name='post'),
    path('cadastrar_post', views.cadastrar_formulario, name='cadastrar_formulario'),
    path('editar_post/<int:id>', views.editar_post, name='editar_post'),
    path('deletar_post/<int:id>', views.deletar_post, name='deletar_post'),
]