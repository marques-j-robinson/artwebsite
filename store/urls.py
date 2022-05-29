from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
]
