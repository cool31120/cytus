from django.shortcuts import render, redirect
from cytus.settings import LOGIN_URL, MAIN_URL
import datetime


def admin_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(LOGIN_URL)
        if request.user.username != 'admin':
            return redirect(MAIN_URL)
        return fun(request, *args, **kwargs)
    return auth


def main(request):
    now = datetime.datetime.now()
    context = {'now':now}
    return render(request, 'main/main.html', context)


def about(request):
    return render(request, 'main/about.html')
