from django.urls import path
from .views import Home,BookDetail,BookUpdateView,BookDeleteView,BookCreateView,BookSearchView
urlpatterns =[
    path('',Home.as_view(), name='home'), 
    path('book/<int:book_id>/', BookDetail.as_view(), name='detail'),
    path('book/update/<int:book_id>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:book_id>/', BookDeleteView.as_view(), name='book_delete'),
    path('book/create/', BookCreateView.as_view(), name='book_create'), 
    path('search/', BookSearchView.as_view(), name='book_search'),
    
    ]