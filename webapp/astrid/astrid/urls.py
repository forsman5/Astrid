from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # setting the default routes directly to website app
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]