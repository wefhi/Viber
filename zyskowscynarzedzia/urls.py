from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('music.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),


]

