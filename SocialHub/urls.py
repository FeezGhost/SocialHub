from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.loginred),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("library/", include("content_libraries.urls")),
    path("gallery/", include("contentGallery.urls")),
    path("calender/", include("calenders.urls"))
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
