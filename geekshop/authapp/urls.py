from django.urls import path
from .views import login, logout, register, edit


app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
]


# from django.urls import path
#
# import authapp.views as authapp
#
# app_name = 'authapp'
#
# urlpatterns = [
#     path('login/', authapp.login, name='login'),
#     path('logout/', authapp.logout, name='logout'),
# ]