from django.shortcuts import render, redirect
import random
from .models import Shrink
import string
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "index.html")


def createshorturl(request):
    if request.method == 'POST':
        slug = ''.join(random.choice(string.ascii_letters)
                       for x in range(10))

        url = request.POST["url"]
        new_url = Shrink(url=url, slug=slug)
        new_url.save()

        messages.info(request, 'New url is created you can check it on view urls')
        return redirect('/')


def urlcreated(request):
    url = Shrink.objects.all()
    return render(request, 'urls.html', {'url': url})
