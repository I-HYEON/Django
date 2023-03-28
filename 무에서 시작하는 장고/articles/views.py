from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'articles/index.html',context)

def detail(request,id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    return render(request,'articles/detail.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)  # 내용이 담겨있는 폼으로 객체 생성
        article = form.save()  # 저장 후 만들어진 객체를 article에 담기
        return redirect('articles:detail',article.id)
    else:
        form = ArticleForm()  # 빈 폼 만들고
    
    context = {'form':form}
    return render(request,'articles/create.html',context)

def update(request,id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # 내용이 담겨있는 폼으로 객체 생성
        form.save()  # 저장 후 만들어진 객체를 article에 담기
        return redirect('articles:detail',article.id)
    else:
        form = ArticleForm(instance=article)  # 빈 폼 만들고
    
    context = {'form':form,'article':article}
    return render(request,'articles/update.html',context)

def delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')