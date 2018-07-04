from django.shortcuts import render
from tapp.views import *
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def gallery(request):
    return render(request,'gallery.html')
def gallery2(request):
    return render(request,'gallery2.html')
def gallery3(request):
    return render(request,'gallery3.html')
def gallery4(request):
    return render(request,'gallery4.html')
def gallery5(request):
    return render(request,'gallery5.html')
def gallery6(request):
    return render(request,'gallery6.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def menu(request):
    category1=Categories.objects.all()
    default_category='cakes'
    all_products=Products.objects.filter(category__slug=default_category)

    return render(request,'menu.html',{'cat':category1,'pro':all_products,'p':default_category})
def item2(request,slug):
    print(slug)
    category1=Categories.objects.all()
    all_products=Products.objects.filter(category__slug=slug)
    #return HttpResponse('hello')
    return render(request,'menu1.html',{'cat':category1,'pro':all_products,'p':slug})
def detail(request,s):
    all_item=Products.objects.get(slug=s)
    return render(request,'detail.html',{'d':all_item})

def elements(request):
    return render(request,'elements.html')
def bloghome(request):
    return render(request,'blog-home.html')
def blogsingle(request):
    return render(request,'blog-single.html')
