from django.urls import path
from . import views 

app_name = "games"

urlpatterns = [
    path('', views.game_list, name="list"),
    path('<slug:slug>', views.game_detail, name="detail")
]
