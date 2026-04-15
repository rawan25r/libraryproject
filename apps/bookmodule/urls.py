from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutus, name='aboutus'),
    path('list/', views.list_books, name='list_books'),
    path('book/<int:book_id>/', views.view_one_book, name='view_one_book'),
    path('html5/links', views.links_page, name='links'),
    path('html5/text/formatting', views.text_formatting_page, name='text_formatting'),
    path('html5/listing', views.listing_page, name='listing'),
    path('html5/tables', views.tables_page, name='tables'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('all', views.list_all_books, name='list_all_books'),


    path('lab8/task1/', views.lab8_task1),
    path('lab8/task2/', views.lab8_task2),
    path('lab8/task3/', views.lab8_task3),
    path('lab8/task4/', views.lab8_task4),
    path('lab8/task5/', views.lab8_task5),
    path('lab8/task7/', views.students_per_city),
    path('lab8/seed/', views.seed_all_data, name='seed_all'),



]
