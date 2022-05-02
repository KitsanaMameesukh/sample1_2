from django.urls import path
from . import views
urlpatterns = [
    # path('', views.todolist),
    path('api/', views.api.as_view()),
    path('create/', views.create),
    path('reply/<int:pk>', views.reply)

]
