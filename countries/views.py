from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import davlat
from .forms import CountryForm
# Create your views here.

class ListView(View):
    def get(self, request):
        davlatlar=davlat.objects.all()
        return render(request, 'index.html', {'davlatlar': davlatlar})

class DetailView(View):
    def get(self, request, pk):
        davlat_c = get_object_or_404(davlat, pk=pk)
        return render(request, 'detail.html', {'davlat_c': davlat_c})



class CreateCountry(View):
    def get(self, request):
        form = CountryForm()
        return render(request, 'create_country.html', {'form': form})

    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create_country.html', {'form': form})




class UpdateCountry(View):
    def get(self, request, pk):
        davlat_c = davlat.objects.get(id=pk)
        form = CountryForm(instance=davlat_c)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        davlat_c = davlat.objects.get(id=pk)
        form = CountryForm(request.POST, instance=davlat_c)
        if form.is_valid():
            form.save()
            return redirect('detail', davlat_c.pk)

class DeleteCountry(View):
    def get(self, request, pk):
        davlat_c = get_object_or_404(davlat, pk=pk)
        return render(request, 'delete.html', {'davlat_c': davlat_c})

    def post(self, request, pk):
        davlat_c = get_object_or_404(davlat, pk=pk)
        davlat_c.delete()
        return redirect('index')

    # def post(self, request):
    #     form = CountryForm(request.POST)
    #     if form.is_valid():
    #         davlat_c = davlat.objects.create(
    #             nomi=form.cleaned_data['nomi'],
    #             poytaxti=form.cleaned_data['poytaxti'],
    #             maydoni=form.cleaned_data['maydoni'],
    #             aholi_soni=form.cleaned_data['aholi_soni'],
    #             tili=form.cleaned_data['tili'],
    #             pul_birligi=form.cleaned_data['pul_birligi'],
    #             qitasi=form.cleaned_data['qitasi'],
    #         )
    #         return redirect('index')
    #     else:
    #         return render(request, 'create_country.html', {'form': form})