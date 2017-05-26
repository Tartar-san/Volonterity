from django.shortcuts import render


def main_page(request):
    if (request.user.is_authenticated):
        return render(request, 'main.html', context={'logged_in': True})
    else:
        return render(request, 'main.html', context={'logged_in': False})


def organization_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'organization-inside.html')
    else:
        return render(request, 'organization-inside.html')


def organization_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'organization-outside.html')
    else:
        return render(request, 'organization-outside.html')


def event_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'event-inside.html')
    else:
        return render(request, 'event-inside.html')


def event_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'event-outside.html')
    else:
        return render(request, 'event-outside.html')


def search(request):
    if (request.user.is_authenticated):
        return render(request, 'search.html')
    else:
        return render(request, 'search.html')


def our_team(request):
    if (request.user.is_authenticated):
        return render(request, 'our-team.html')
    else:
        return render(request, 'our-team.html')


def enter(request):
    if (request.user.is_authenticated):
        return render(request, 'enter.html')
    else:
        return render(request, 'enter.html')


def user_inside(request):
    if (request.user.is_authenticated):
        return render(request, 'user-inside.html')
    else:
        return render(request, 'user-inside.html')


def user_outside(request):
    if (request.user.is_authenticated):
        return render(request, 'user-outside.html')
    else:
        return render(request, 'user-outside.html')

def about_us(request):
    if (request.user.is_authenticated):
        return render(request, 'about-us.html')
    else:
        return render(request, 'about-us.html')






