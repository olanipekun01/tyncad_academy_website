from django.shortcuts import render, redirect
from datetime import datetime


#load homepage and list of post that were published
def index(request):
    return render(request, 'common/base.html')
