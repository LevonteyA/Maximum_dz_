from django.shortcuts import render, redirect
from .models import OnlineShop
from .forms import OnlineShopForm
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
def index(request):
    #выгружаем объекты из базы
    online_shops = OnlineShop.objects.all()
    #cоздаём контекст
    context = {'online_shops': online_shops}
    return render(request, 'app_advertisement/index.html', context)
#функция отображающая файл top-sellers.html
def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

#функция для отображения формы объявления на сайте
def advertisement_post(request):
    #проверка, что обрабатывается post запрос
    if request.method == 'POST':
        form = OnlineShopForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = OnlineShop(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = OnlineShopForm()
    context = {'form':form}
    return render(request, 'app_advertisement/advertisement-post.html', context)