from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import davlat
from .forms import CountryForm
# Create your views here.

class ListView(View):
    def get(self, request):
        davlatlar=davlat.objects.all()
        return render(request, 'index.html', {'davlatlar': davlatlar})

class CreateCountry(View):
    def get(self, request):
        form = CountryForm()
        return render(request, 'create_country.html', {'form': form})

    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            davlat_c = davlat.objects.create(
                nomi=form.cleaned_data['nomi'],
                poytaxti=form.cleaned_data['poytaxti'],
                maydoni=form.cleaned_data['maydoni'],
                aholi_soni=form.cleaned_data['aholi_soni'],
                tili=form.cleaned_data['tili'],
                pul_birligi=form.cleaned_data['pul_birligi'],
                qitasi=form.cleaned_data['qitasi'],
            )
            return redirect('index')
        else:
            return render(request, 'create_country.html', {'form': form})