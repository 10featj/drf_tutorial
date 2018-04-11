from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
