
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

from apps.products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('users/', include('apps.users.urls', namespace='')),
    path('orders/', include('apps.orders.urls', namespace='')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

