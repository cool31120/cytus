from django.shortcuts import render

def record(request):
    return render(request, 'record/record.html')
