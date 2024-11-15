from django.urls import path
from .views import projects_list # Import both views here

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', projects_list, name='projects'),
  
]

# Serve media files in development (only when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)