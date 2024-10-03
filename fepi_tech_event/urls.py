from django.urls import path
from poesias.views import root_view, home

urlpatterns = [
    path('', root_view),
    path('home/', home),
]