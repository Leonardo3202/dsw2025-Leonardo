from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

def lista_posts(request):
    posts = Post.objects.filter(aprovado=True).order_by('-criado_em')
    return render(request, 'posts/lista_posts.html', {'posts': posts})

@login_required
def criar_post(request):
    erro = None

    if request.method == 'POST':
        comentario = request.POST.get('comentario', '').strip()
        foto = request.FILES.get('foto')

        if not comentario and not foto:
            erro = 'Você precisa escrever um comentário ou enviar uma foto.'
        else:
            aprovado = request.user.is_staff or request.user.is_superuser

            Post.objects.create(
                comentario=comentario,
                foto=foto,
                autor=request.user,
                aprovado=aprovado
            )
            return redirect('lista_posts')

    return render(request, 'posts/criar_post.html', {'erro': erro})

