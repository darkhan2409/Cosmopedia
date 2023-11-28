from django.urls import path
from .views import *

urlpatterns = [
    path('api/', CategoryApiView.as_view()),
    path('api/<int:pk>/', CategoryDetailApiView.as_view()),
]