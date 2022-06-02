from django.urls import path
from . import views as vs

app_name = 'noteapp'

urlpatterns = [

    path('', vs.home, name='home'),
    path('create-note/', vs.create_note, name='create-note'),
    path('update-note/<str:pk>/', vs.update_note, name='update-note'),
    path('delete_note/', vs.delete_note, name='delete_note'),
    path('create-category/', vs.create_category, name='create-category'),
    path('categoryList/', vs.category_page, name='category-page'),
    path('delete-category/<str:pk>/', vs.delete_category, name='delete-category'),
    path('template/', vs.template, name='template'),
]
