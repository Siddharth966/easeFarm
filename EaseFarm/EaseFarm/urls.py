from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "EaseFarm"
admin.site.site_title = "EaseFarm"
admin.site.index_title = "Welcome to EaseFarm"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
