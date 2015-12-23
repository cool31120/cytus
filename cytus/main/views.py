from django.shortcuts import render
import datetime


def main(request):
    now = datetime.datetime.now()
    context = {'like':'Cytus是雷亞公司的處女作', 'now':now}
    return render(request, 'main/main.html', context)


def about(request):
    return render(request, 'main/about.html')