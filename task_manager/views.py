from django.shortcuts import render


def index(request):
    return render(
        request,
    'index.html',
        context={
            'title': 'главная Task-manager',
            'hello': 'Привет от Task-manager',
        }
    )