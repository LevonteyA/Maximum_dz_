from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import  reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
# создаём отоюражение профиля
@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return  render(request, 'app_auth/profile.html')

# создаём аутентификацию пользователя
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    user_name = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, user_name, password)
    #проверка что нашлась комбинация
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    #не нашлась
    return render(request, 'app_auth/login.html', {'error':'Пользователь не найден'})
#создаём выход
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})