from django.conf.urls import url

from .views import ListSubredditView


urlpatterns = [
    url(r'list/?$', ListSubredditView.as_view(), name='list'),
]
