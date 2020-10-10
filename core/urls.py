from django.urls import path
from .views import Products, home, checkout

app_name = 'core'

urlpatterns = [
	path('', home, name='home'),
	path('products/', Products, name='products'),
	path('checkout/', checkout, name='checkout'),	
]