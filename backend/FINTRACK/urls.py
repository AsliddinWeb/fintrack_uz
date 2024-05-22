from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "FinTrack Uz | Admin"
admin.site.site_header = "FintrackUz"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    # path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)