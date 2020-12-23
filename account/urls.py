from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('signout/',views.signout,name='signout'),
]
