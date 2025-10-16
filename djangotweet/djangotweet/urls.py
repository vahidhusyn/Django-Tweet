
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
from tweet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('', views.tweet_list, name='tweet_list'),
    path('accounts/', include('django.contrib.auth.urls')),

   path("convert/", include("guest_user.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
