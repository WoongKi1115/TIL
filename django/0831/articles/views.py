from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    content = {
        'articles': articles
    }
    return render(request, 'articles/index.html', content)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
