from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.Index_view,name="home"),
    path('sign-up/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('^profile/',views.profile,name="profile"),
]