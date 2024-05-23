from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Chart
from .views import DataView

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

urlpattern_basic = [
    path("admin/", admin.site.urls),

    # Docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Api
    path('api/v1/auth/', include('account_app.urls')),
    path('api/v1/expense/', include('expense_app.urls')),
    path('api/v1/income/', include('income_app.urls')),
    path('api/v1/ai/', include('ai_app.urls')),

    # Auth

]

urlpattern_chart = [
    path('api/v1/chart/daily/', DataView.as_view(), {'period': 'daily'}, name='daily-data'),
    path('api/v1/chart/weekly/', DataView.as_view(), {'period': 'weekly'}, name='weekly-data'),
    path('api/v1/chart/monthly/', DataView.as_view(), {'period': 'monthly'}, name='monthly-data'),
    path('api/v1/chart/yearly/', DataView.as_view(), {'period': 'yearly'}, name='yearly-data'),
]

urlpatterns = urlpattern_basic + urlpattern_chart

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)