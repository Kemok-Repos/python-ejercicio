from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('handle/', include('handle_scrapping_data_module.routers')),
]
