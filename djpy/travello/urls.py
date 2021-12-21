from django.urls import path,include
from .  import views
urlpatterns=[path("",views.index,name="index"),
            # path("about.html",views.about,name="About Us"),
            # path("contact.html",views.contact,name="contact"),
            # path("destinatins.html",views.destinations,name="destinations"),
            # path("elements.html",views.elements,name="elements"),
            # path("news.html",views.news,name="news")
            
]