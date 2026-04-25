from django.urls import path
from . import views

app_name = "bookmodule"

urlpatterns = [
    path('', views.index, name='index'),

    # Lab 8
    path('lab8/task1/', views.lab8_task1),
    path('lab8/task2/', views.lab8_task2),
    path('lab8/task3/', views.lab8_task3),
    path('lab8/task4/', views.lab8_task4),
    path('lab8/task5/', views.lab8_task5),
    path('lab8/task7/', views.students_per_city),
    path('lab8/seed/', views.seed_all_data, name='seed_all'),

    # Lab 9
    path('lab9/task1/', views.task1),
    path('lab9/task2/', views.task2),
    path('lab9/task3/', views.task3),
    path('lab9/task4/', views.task4),
    path('lab9/task5/', views.task5),
    path('lab9/task6/', views.task6),
    path("seed/", views.seed_data, name="seed"),

]
