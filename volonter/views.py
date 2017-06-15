import thread
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm, EventForm
from django.core.mail import send_mail
from django.conf import settings
from .models import *

import random
import string

def generate_random_string(chars=string.ascii_uppercase +
                                                  string.ascii_lowercase + string.digits):
    size = random.randint(10, 12)
    return ''.join(random.choice(chars) for _ in range(size))

def confirmation_email(email, link):
    ripka_email = settings.EMAIL_HOST_USER
    subject = 'Підтвердження реєстрації'
    message = 'Ви отримали цей лист, тому що на ваш емейл було зареєстровано користувача' \
              'на волонтерській платформі Ripka. \n' \
              'Для підтвердження реєстрації перейдіть за лінком: \n' + link
    send_mail(subject, message, ripka_email, [email], fail_silently=False)

def main_page(request): #
    events = Event.objects.all()
    if (request.user.is_authenticated):
        return render(request, 'main.html', context={'logged_in': True, 'events': events})
    else:
        return render(request, 'main.html', context={'logged_in': False, 'events': events})


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


def user_registration(request):
    if (request.method == 'POST'):
        form = UserForm(request.POST)

        if form.is_valid():
            url = "127.0.0.1:8000/confirm/" + generate_random_string()
            thread.start_new_thread(confirmation_email(form.changed_data['email'], url))
            return redirect('/final_step')


    else:
        form = UserForm()

    return render(request, 'user_registration.html', context={"logged_in": False, "form": form})

def create_event(request):
    if (request.method == 'POST'):
        form = EventForm(request.POST)

        if form.is_valid():
            event = Event(creator=request.user, title=form.title, city=form.city, event_type=form.event_type)
            event.save()
            event_img = EventImages(event=event, image=form.image, short_description="lol")
            event_img.save()
            return redirect('/')
    else:
        form = EventForm()

    return render(request, 'create_event.html', context={"logged_in": True, "form": form})

def create_organization(request):
    return redirect('/not_available')


def custom404_view(request):
    return render(request, '404page.html')

def after_registration_view(request):
    return render(request, 'check_email_after_registration.html', context={'logged_in': False})

def confirm_registration(request, string):
    return render(request, 'registration_confirmed.html', context={'logged_in': False})


