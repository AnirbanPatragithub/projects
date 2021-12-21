from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    # dest1=Destination()
    # dest1.name='Mumbai'
    # dest1.img='destination_1.jpg'
    # dest1.desc='The CITY that never sleeps'
    # dest1.price=299
    # dest1.offer=False

    # dest2=Destination()
    # dest2.name='Darjeeling'
    # dest2.img='destination_2.jpg'
    # dest2.desc='Beautiful Nature'
    # dest2.price=399
    # dest2.offer=False

    # dest3=Destination()
    # dest3.name='Howrah Bridge'
    # dest3.img='destination_3.jpg'
    # dest3.desc='The Link'
    # dest3.price=499
    # dest3.offer=True

    # dest4=Destination()
    # dest4.name='India Gate'
    # dest4.desc='The Gateway'
    # dest4.img='destination_4.jpg'
    # dest4.price=599
    # dest4.offer=False

    # dest5=Destination()
    # dest5.name='Goa'
    # dest5.img='destination_5.jpg'
    # dest5.desc='Beautiful Beaches'
    # dest5.price=699
    # dest5.offer=False

    # dest6=Destination()
    # dest6.name='Studio'
    # dest6.img='destination_6.jpg'
    # dest6.desc='countryside'
    # dest6.price=799
    # dest6.offer=False
    dests=Destination.objects.all
    return render (request,"index.html",{'dests':dests})
    #return render (request,"index.html",{'dest1':dest1,'dest2':dest2,'dest3':dest3,'dest4':dest4,'dest5':dest5,'dest6':dest6})