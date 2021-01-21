from django.urls import path
from home.views import helloworld

urlpatterns = [
    path('', helloworld),
]

