from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

# GET 방식 : 특정 리소스 조회 (보안이 필요없다. ex 네이버 검색)
# POST 방식 : 특정 리소스 변경(보안성이 필요하다 ex 아이디 비번)
#               -> Token 확인 : DB에 조작을 가하는 요청은 반드시 인증 수단 필요

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title = title, content = content)
    # article.save()

    # return render(request, 'articles/create.html')
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk = pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk = pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.htrml', context)
