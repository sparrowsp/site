from django.shortcuts import render, get_object_or_404
from .models import Image

def image_list(request):
    images = Image.objects.all()
    return render(request, 'art/image/list.html', {'images': images})

def image_detail(request, year, month, day, image):
    image = get_object_or_404(Image, slug=image,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'art/image/detail.html', {'image': image})