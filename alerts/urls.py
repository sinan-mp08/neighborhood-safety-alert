from django.urls import path
from . import views
from .views import CustomLoginView
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('alerts/', views.alerts_list_view, name='alerts_list'),
    path('report/', views.report_incident_view, name='report_incident'),
    
]
