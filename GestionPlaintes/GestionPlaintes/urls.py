from django.contrib import admin
from django.urls import path, include
from GestionPlaintes import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('acceuil/', include('UserPart.urls')),
    path('responsible/', include('BackOffice.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

