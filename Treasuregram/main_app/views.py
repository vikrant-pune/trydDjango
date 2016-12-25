from django.shortcuts import render

from models import Treasure

# from django.http import

# Create your views here.



def index(request):
    return render(request, 'index.html', {'treasures': Treasure.objects.all()
                                          })


def detail(request, id):
    treasure = Treasure.objects.get(id=id)
    return render(request, 'detail.html', {'treasure': treasure})
