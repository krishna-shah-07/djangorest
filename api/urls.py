from django.urls import path, include
from expense import views

urlpatterns = [
    path('transactions/', views.get_transactions),
]