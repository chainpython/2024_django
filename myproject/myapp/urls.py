from django.urls import path
from . import views

from .views import iframe_view, convert_utm
urlpatterns = [
    #path('', views.home, name='home'),
    path('', iframe_view, name='iframe_page'),
    path('convert_utm/', convert_utm, name='convert_utm'),
]

