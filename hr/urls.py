from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('create', views.create, name='create'),
    path('edit_employee/<int:pk>', views.edit_employee, name='edit_employee'),
]