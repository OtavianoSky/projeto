from django.urls import path
from .views import PollsView

urlpatterns = [
    # path('endereço/', Minhaview.as_view(), name='nome_da_url'),
    path('votacao/', PollsView.as_view(), name='votacao'),

]