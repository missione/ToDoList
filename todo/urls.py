from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="main"),
    path('updateTodo/<str:pk>/',views.updateTask,name="updateTodo"),
    path('delete/<str:pk>/',views.deleteTask,name="deleteTodo"),
]