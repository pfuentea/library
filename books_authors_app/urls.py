from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new_book/', views.new_book),
    path('book_view/<int:id_book>', views.book_view),
    path('add_author/', views.add_author ),

    path('authors/', views.authors),
    path('new_author/', views.new_author),
    path('author_view/<int:id_author>', views.author_view),    
    path('add_book/<int:author_id>', views.add_book),
]
