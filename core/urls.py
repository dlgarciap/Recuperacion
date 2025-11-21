from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('creditos/', views.creditos, name='creditos'),
]