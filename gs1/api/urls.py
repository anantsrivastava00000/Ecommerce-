from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('go-to-cart/', views.go_to_cart, name='go-to-cart'),
    path('remove-from-cart/<int:id>', views.remove_from_cart, name='remove-from-cart'),
    path('search/', views.search, name='search'), 
    path('update-cart/<int:id>', views.update_cart, name='update-cart'), 
    path('delete-cart/<int:id>', views.delete_cart, name='delete-cart'), 
]