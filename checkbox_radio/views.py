from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import Check_boxForm, RadioForm, PostForm


def mostrar_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post.html', {'post': post})


def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post_form = PostForm(instance=post)

    if request.method == 'GET':
        return render(request, 'editar_post.html', {'post_form': post_form, 'post': post})


    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            print('Editado com sucesso')
            post_form.save()
            return redirect('/')


def cadastrar_formulario(request):

    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'cadastrar_post.html', {'post_form': post_form})

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            print('Formulario enviado')
            post_form.save()
            return redirect('/')
        

def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/')


    
    