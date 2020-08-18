from django.urls import path
from ajaximage import views

urlpatterns = [
    path(r'^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
         views.ajaximage,
         name='ajaximage'),
]
