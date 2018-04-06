from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'comics_list_app/index.html')