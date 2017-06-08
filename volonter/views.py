from django.shortcuts import render


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






