from django.urls import path
from . import views

# Airline requests.
airline_urls = [
    path('airline/<uuid:pk>/', views.aircraft_delete, name='aircraft-delete'),
    path('airline/<str:pk>/', views.chain_get_patch_delete, name='airline-chain-get-patch-delete'),
    path('airline/', views.chain_list_post, name='airline-chain-list-post'),
]