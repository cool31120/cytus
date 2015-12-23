from django.shortcuts import render
import datetime


def main(request):
    now = datetime.datetime.now()
    context = {'like':'地獄章節L章已經來臨', 'now':now}
    return render(request, 'main/main.html', context)


def about(request):
    return render(request, 'main/about.html')