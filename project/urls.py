from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from project.admin import owners_admin, admin

urlpatterns = [
    url(r'^admin/', admin.urls),
    url(r'^owners-admin/', owners_admin.urls),
    url(r'^', include('pets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

