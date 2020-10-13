from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('buyer.urls')),
    path('community/', include('community.urls')),
    path('', include('meta.urls')),
    path('admin/', admin.site.urls),
]
