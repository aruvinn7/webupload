
from django.urls import path
from . import views

urlpatterns = [
    # Voter URLs
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Vote URLs
    path('read_vote/', views.read_vote, name='read_vote'),
    path('delete_vote/', views.delete_vote, name='delete_vote'),

]
