from django.urls import path
from .views import *

urlpatterns = [
    path('api/', ArticleApiView.as_view()),
]