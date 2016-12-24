from django.shortcuts import render

import models


# from django.http import

# Create your views here.



def index(request):
    return render(request, 'index.html', {'treasures': models.Treasure.objects.all()
                                          })
