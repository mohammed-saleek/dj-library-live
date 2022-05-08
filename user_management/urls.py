from django.urls import path,include
from .import views


urlpatterns = [
    path('Registration/', views.user_register, name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name = 'logout'),
]