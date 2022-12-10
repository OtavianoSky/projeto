from django.urls import path
from .views import IndexView

urlpatterns = [
    # path('endereço/', Minhaview.as_view(), name='nome_da_url'),
    path('inicio/', IndexView, name='inicio'),

]