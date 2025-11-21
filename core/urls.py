from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(url='/usuarios/'), name='home'),  # ← Redirige raíz a usuarios
    path('creditos/', views.creditos, name='creditos'),
]