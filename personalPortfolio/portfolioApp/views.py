from django.shortcuts import render
from .forms import PortfolioForm

# Create your views here.

def Homepage(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'templates/index.html', context={"form":"Message send sucess!"})
        return render(request, 'templates/index.html', context={"form":"Message send fail!"})
    return render(request, 'templates/index.html')

