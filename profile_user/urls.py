from django.urls import path
from .views import page_web_profile_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path("api/profile/", page_web_profile_user.as_view(), name="profile")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)