from django.shortcuts import render, get_object_or_404
from .models import Emage

def emage_list(request):
    emages = Emage.objects.all()
    return render(request, 'blog/emage/list.html', {'emages': emages})

