from django.contrib import admin
from django.urls import re_path ,path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    re_path('games/', include('games.urls')),
    re_path('accounts/', include('accounts.urls')),
    path('', views.home)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)