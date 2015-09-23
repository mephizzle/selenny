from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('selenny.apps.main.urls')),
]
