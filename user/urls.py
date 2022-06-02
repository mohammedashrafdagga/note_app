from django.urls import path
from . import views as vs

app_name = 'userapp'
urlpatterns = [

    path('sign-up/', vs.signup, name='sign-up'),
    path('userprofile/<str:username>/', vs.userprofile, name='userprofile'),
]
