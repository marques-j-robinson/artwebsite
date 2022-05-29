from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('summary/', views.summary, name='cart_summary'),
]
