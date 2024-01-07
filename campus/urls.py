from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logout-user/', views.logout_user, name='logout-user'),
    path('user-login/', views.user_login, name='user-login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user-report/', views.user_report, name='user-report'),
    path('about/', views.about, name='about'),
    path('visitors/', views.visitors, name='visitors'),
    path('reports/', views.report, name='reports'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('delete/<int:id>', views.delete, name='delete'),
]