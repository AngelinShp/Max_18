from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# Create your views here.
# прописываем, что можно вернуть на к-нибудь запрос
def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements': advertisements}
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
