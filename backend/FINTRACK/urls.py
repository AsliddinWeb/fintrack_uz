from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Swagger UI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="FinTrack Uz | API",
      default_version='v1',
      description="FinTrack Uz",
   ),
    public=True
)


admin.site.site_title = "FinTrack Uz | Admin"
admin.site.site_header = "FintrackUz"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),

    # Docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Api
    path('api/v1/auth/', include('account_app.urls')),
    path('api/v1/expense/', include('expense_app.urls')),
    path('api/v1/income/', include('income_app.urls')),
    path('api/v1/ai/', include('ai_app.urls')),

    # Auth
    # path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)