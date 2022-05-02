from django.urls import path
from . import views
urlpatterns = [
    # path('', views.todolist),
    path('api/', views.api.as_view()),
    path('api/<int:pk>', views.detail.as_view()),
    path('create/', views.createTodo),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete)
]
