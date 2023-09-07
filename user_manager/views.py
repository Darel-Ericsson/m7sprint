from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import *

# Create your views here.
def index(request):
    context = {}
    # return render(request, "index.html", context)

def welcome(request):
    context = {}
    return render(request, 'welcome.html', context)

def signin(request):
    if request.method == 'GET':
        context = {'form': AuthenticationForm}
        return render(request, 'auth/signin.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return JsonResponse({'success': False, 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return JsonResponse({'success': True})


from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        formulario_post = CustomCreationForm(request.POST)
        if formulario_post.is_valid():
            user = formulario_post.save()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            # Return form errors as JSON response
            return JsonResponse({'success': False, 'errors': formulario_post.errors})
    else:
        return render(request, 'auth/signup.html', {
            'form' : CustomCreationForm()
        })


def signout(request):
    logout(request)
    return redirect('user_manager:welcome')
