from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include(('novoProjeto.core.urls', 'core'), namespace='core')),
    url(r'^conta/', include(('novoProjeto.accounts.urls','accounts'), namespace='accounts')),
    url(r'^cursos/', include(('novoProjeto.courses.urls', 'courses'), namespace='courses')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
