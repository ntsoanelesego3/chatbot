from django.urls import path
from . import views
urlpatterns = [
    path('cal/',views.cal, name='cal'),
    path('login/',views.login,name='login'),
    path('register/',views.register),

]
