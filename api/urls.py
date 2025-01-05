from django.urls import path, include
from expense import views

urlpatterns = [
    path('transactions/', views.get_transactions),
    path('transactions-all/', views.TransactionAPI.as_view()), # class based view
]