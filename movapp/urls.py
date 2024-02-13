from django.urls import path
from . import views

app_name = 'movapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('dlt/<int:id>/', views.delet, name='delet'),
]
