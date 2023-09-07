from django.urls import path
from . import views

app_name = 'user_manager'
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.welcome, name="welcome"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
]