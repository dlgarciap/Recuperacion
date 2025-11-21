from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def creditos(request):
    return render(request, 'core/creditos.html')