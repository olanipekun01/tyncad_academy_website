from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request, 'common/base.html')
