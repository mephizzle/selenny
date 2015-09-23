from django.conf.urls import url

from selenny.apps.main.views import HowToView, SelennyView


urlpatterns = [
    url(r'^(?P<start>\d+)/(?P<number>\d+)/$', SelennyView.as_view()),
    url(r'^$', HowToView.as_view())
]
