from django.urls import path
from . import views 
app_name='registration'
urlpatterns=[
    path('', views.home, name ='home'),
    # path('success/', views.success, name='success'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('aboutus', views.about, name='aboutus'), 

]