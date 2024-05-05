from django.contrib import admin
from django.urls import path
from votingapp import views
from django.urls import path 

# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("",views.index,name='home'),
    path("login/",views.login,name='login'),
    path("signup/",views.signup,name='signup'),
    # path('contact/', views.contact_view, name='contact'),
]

