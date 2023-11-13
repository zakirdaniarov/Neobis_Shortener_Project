from django.urls import path
from .views import Make, Home, LinkListCreateView

urlpatterns = [
    path('', Make, name='link-list-create'),
    path('<str:token>', Home, name="Home"),
    path('links/', LinkListCreateView.as_view(), name='link-list-create'),
]
