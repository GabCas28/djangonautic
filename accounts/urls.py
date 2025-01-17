from django.urls import path
from . import views 

app_name = "accounts"

urlpatterns = [
    path('singup/', views.singup_view, name="singup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
