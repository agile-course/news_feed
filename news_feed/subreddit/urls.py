from django.conf.urls import url

from .views import CreateSubredditView, ListSubredditView


urlpatterns = [
    url(r'create/?$', CreateSubredditView.as_view(), name='create'),
    url(r'list/?$', ListSubredditView.as_view(), name='list'),
]
