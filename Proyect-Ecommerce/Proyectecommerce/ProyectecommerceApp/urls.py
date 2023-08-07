
from django.urls import path
from ProyectecommerceApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros', views.us, name="nosotros"),
    # path('tienda', views.shop, name="tienda"),

]
