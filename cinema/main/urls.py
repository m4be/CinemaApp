from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name = 'index'),
    path('buy-ticket-elki', views.elki, name='elki'),
    path('buy-ticket-troll', views.troll, name='troll'),
    path('buy-ticket-adam', views.adam, name='adam'),
    path('buy-ticket-adams', views.adams, name='adams'),
    path('buy-ticket-amsterdam', views.amsterdam, name='amsterdam'),
    path('buy-ticket-avatar', views.avatar, name='avatar'),
    path('buy-ticket-fall', views.fall, name='fall'),
    path('buy-ticket-fallout', views.fallout, name='fallout'),
    path('buy-ticket-heart', views.heart, name='heart'),
    path('buy-ticket-panther', views.panther, name='panther'),
    path('buy-ticket-potter', views.potter, name='potter'),
    path('buy-ticket-shel', views.shel, name='shel'),
    path('about-us',views.about, name = 'about'),


    path('buy-ticket', views.buyTicketTESTDELETEE,name='TEST')

]
