from django.urls import path
from . import views

aircraft_urls = [
    path('aircraft/<uuid:pk>/', views.chain_get_patch_delete, name='aircraft-chain-get-patch'),
    path('aircraft/', views.chain_list_post, name='aircraft-chain-list-post')
]