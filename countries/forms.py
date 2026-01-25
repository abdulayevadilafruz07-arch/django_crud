from django import forms

from countries.models import davlat



# class CountryForm(forms.Form):
#     nomi = forms.CharField(max_length=100)
#     poytaxti =forms.CharField(max_length=100)
#     maydoni = forms.FloatField()
#     aholi_soni = forms.IntegerField()
#     tili = forms.CharField(max_length=200)
#     pul_birligi = forms.CharField(max_length=50)
#     qitasi = forms.CharField(max_length=50)

class CountryForm(forms.ModelForm):
    class Meta:
        model = davlat
        fields = ['nomi','poytaxti','maydoni','aholi_soni','tili','pul_birligi','qitasi']
