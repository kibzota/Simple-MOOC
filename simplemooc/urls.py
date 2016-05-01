from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^conta/', include('accounts.urls', namespace="accounts")),
    url(r'^', include('core.urls', namespace="core")),
    url(r'^cursos/', include('courses.urls', namespace="courses")),
    url(r'^forum/', include('forum.urls', namespace="forum")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
