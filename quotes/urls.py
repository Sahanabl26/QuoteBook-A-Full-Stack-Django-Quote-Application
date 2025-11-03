from django.urls import path
from . import views
from quotes.views import login

urlpatterns = [
    path('home/', views.home, name="home"),
    path('quotes/', views.all_quotes, name="all_quotes"),
    path('add/', views.add_quote, name="add_quote"),
    path('like/<int:quote_id>/', views.like_quote, name='like_quote'),
    path('login/', views.login, name='login'),  
    path('signup/', views.signup, name='signup'),
    path('', views.signup, name='signup'), 
    path('author/<str:author_name>/', views.author_quotes, name='author_quotes'),
    path('logout/', views.logout_view, name='logout'),
]
