from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.Index_view,name="home"),
    path('sign-up/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('^profile/',views.profile,name="profile"),
    path('^addstory/$',views.new_story,name="new_story"),
    path('^myprofile/$',views.person_info,name="user_profile"),
    path('^addbusiness/$',views.new_business,name="register-business"),
    path('^hood-contacts/$',views.show_contact,name="show-contact")

]