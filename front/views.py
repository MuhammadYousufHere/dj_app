from django.shortcuts import render
from django.http import HttpRequest


def front(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'base.html')
