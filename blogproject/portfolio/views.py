from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})

def writepf(request):
    return render(request, 'portfolio/writepf.html')

def createpf(request):
    portfolio = Portfolio()
    portfolio.title = request.POST.get('title', '').strip()
    portfolio.description = request.POST.get('description', '').strip()
    portfolio.image = request.FILES.get('image')
    portfolio.pub_date = timezone.datetime.now()
    portfolio.save()
    return redirect('/portfolio')