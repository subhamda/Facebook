from django.urls import path
from .  import views

urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("profile",views.profile,name="profile"),
    path("Login",views.Login,name="Login"),
    path("Logout",views.Logout,name="Logout"),
    path("Register",views.Register,name="Register"),
]