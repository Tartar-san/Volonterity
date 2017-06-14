from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm
from .models import *

def main_page(request): #
    if (request.user.is_authenticated):
        return render(request, 'main.html', context={'logged_in': True})
    else:
        return render(request, 'main.html', context={'logged_in': False})


def organization_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'organization-inside.html', context={'logged_in': True})
    else:
        return render(request, 'organization-inside.html', context={'logged_in': False})


def organization_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'organization-outside.html', context={'logged_in': True})
    else:
        return render(request, 'organization-outside.html', context={'logged_in': False})


def event_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'event-inside.html', context={'logged_in': True})
    else:
        return render(request, 'event-inside.html', context={'logged_in': False})


def event_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'event-outside.html', context={'logged_in': True})
    else:
        return render(request, 'event-outside.html', context={'logged_in': False})


def search(request):
    if (request.user.is_authenticated):
        return render(request, 'search.html', context={'logged_in': True})
    else:
        return render(request, 'search.html', context={'logged_in': False})


def our_team(request):
    if (request.user.is_authenticated):
        return render(request, 'our-team.html', context={'logged_in': True})
    else:
        return render(request, 'our-team.html', context={'logged_in': False})


def enter(request):
    if (request.user.is_authenticated):
        return render(request, 'enter.html', context={'logged_in': True})
    else:
        return render(request, 'enter.html', context={'logged_in': False})


def user_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'user-inside.html', context={'logged_in': True})
    else:
        return render(request, 'user-inside.html', context={'logged_in': False})


def user_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'user-outside.html', context={'logged_in': True})
    else:
        return render(request, 'user-outside.html', context={'logged_in': False})

def about_us(request):
    if (request.user.is_authenticated):
        return render(request, 'about-us.html', context={'logged_in': True})
    else:
        return render(request, 'about-us.html', context={'logged_in': False})


def logout_view(request):
    logout(request)
    return redirect('/')

# GET METHOD
def registration(request):
    if (not request.user.is_authenticated):
        form = UserForm()
        return render(request, 'main-reg.html', context={'logged_in': False, 'form' : form})
    else:
        return redirect('/not_available')

# POST_METHOD
def user_registration(request):
    return redirect('/not_available')

def registration_confirmation(request):
#    user = UserProfile.objects.get(confirmation_url = url)
#    user.confirmed = True
    pass




def custom404_view(request):
    return render(request, '404page.html')

