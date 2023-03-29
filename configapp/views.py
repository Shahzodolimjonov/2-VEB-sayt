from django.shortcuts import render,redirect
from .models import News,Category
from .forms import NewForm


# Create your views here.
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    content = {
        'news':news,
        'categories':categories,
    }
    return render(request,'news/index.html',context=content)

def category(request,pk):
    news = News.objects.filter(category=pk)
    categories = Category.objects.all()
    content = {
        'news':news,
        'categories':categories,
    }
    return render(request,'news/category.html',context=content)

def detail(request,pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    content = {
        'news':news,
        'categories':categories,
    }
    return render(request,'news/detail.html',context=content)

def n_del(request, pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect('home')

def add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewForm()
    categories = Category.objects.all()
    content={
        'form':form,
        'categories':categories,
    }
    return render(request,'news/add_new.html',context=content)

def new_update(request,pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewForm(request.POST,instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewForm(instance=news)
    content = {
        'news':news,
        'form':form,
    }
    return render(request,'news/new_update.html',context=content)
