from django.urls import path
from app import views

urlpatterns=[

     
 path('',views.first,name='first'),
 path('all_expenses', views.all_expenses, name='all_expenses'),
 path('input_expneses', views.input_expneses, name='input_expneses'),
]