from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse 
from django.contrib import auth 
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rolepermissions.roles import assign_role


def cadastrar_vendedor(request):
    if request.method == 'GET':
        vendedores = Users.objects.filter(cargo="V")
        return render(request, 'cadastrar_vendedor.html', {'vendedores': vendedores })

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('Email já existe')

        user = Users.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome,
            last_name=sobrenome,
            cargo='V'
        )

        assign_role(user, 'gerente') 
        
        return render(request, 'cadastrar_vendedor.html')
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('add_produto'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        
        if not user:
            return HttpResponse('Usuario Invalido')
        
        auth.login(request, user)
        return redirect(reverse('add_produto'))
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluido com sucesso')
    return redirect(reverse('cadastrar_vendedor'))
    


