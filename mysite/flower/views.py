from django.shortcuts import render, get_object_or_404
from .models import fl

def fl_list(request):
    fls = fl.objects.all()
    return render(request, 'flower/fl/list.html', {'fls': fls})

