from django.shortcuts import render, redirect
from users.models import CustomUser
from django.views import View




class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')


    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'auth/register.html',{
                "error": "Bu username band"
            })


        if password != confirm_password:
            return render(request, 'auth/register.html',{
                "error": "Parollar mos emas"
            })

        user=CustomUser.objects.create_user(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('index')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')