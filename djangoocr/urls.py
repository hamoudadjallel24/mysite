from django.urls import re_path, path
from . import views

app_name = 'imagetotext'

urlpatterns = [
    path('', views.imagetoText, name='imagetoText'),
]