from django.urls import path
from stocks import views

urlpatterns = [
    path('',views.search_stock,name='SearchStock')
]
