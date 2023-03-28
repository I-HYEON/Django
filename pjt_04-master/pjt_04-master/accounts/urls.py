from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('delete/',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
