from django.contrib import admin
from django.urls import path
from water_monitor import views 
urlpatterns = [
    # CHANGE THIS LINE:
    path('admin/', admin.site.urls), 
    
    # Your main dashboard
    path('', views.dashboard, name='dashboard'),
]