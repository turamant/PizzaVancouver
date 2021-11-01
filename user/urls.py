from django.urls import path

from user.views import UserByToken

urlpatterns = [
    path('by/token/', UserByToken.as_view()),
]