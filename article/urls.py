from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index_view, name='index'),
    path('category/<int:pk>', category_view, name='category'),
    path('article/<int:pk>', article_view, name='article'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('suggestion/', suggestions, name='suggestion'),
    path('save_comment/<int:pk>', save_comment, name='save_comment'),
    path('profile/', profile, name='profile'),
    path('profile/edit_profile/', edit_profile, name='edit_profile'),
    path('profile/edit_account/', edit_account, name='edit_account'),
    path('search/', views.search_view, name='search'),


]