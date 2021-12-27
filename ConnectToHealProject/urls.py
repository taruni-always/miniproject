from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path,include
from userRegister import views as user_views

urlpatterns = [
    path('',include("ConnectToHealMain.urls")),
    path('signup/', user_views.register,name="Register"),
    path('login/', auth_views.LoginView.as_view(template_name='userRegister/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userRegister/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]

