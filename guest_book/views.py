from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def index_view(request):
    print('\n\n\n  >>> HELLO SERVER :) <<< \n\n\n')
    return render(request, 'index.html')

def post_view(request):
    user_name = request.POST['user_name']
    Users(name=user_name, password='').save()
    return HttpResponse('user  <h2> ' + user_name + ' </h2> saved! ')
