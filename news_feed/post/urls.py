from django.conf.urls import url

from .views import CreatePostView, ListPostView


urlpatterns = [
    url(r'(?P<subreddit_scope>(.*))/create/?$', CreatePostView.as_view(), name='create'),
    url(r'(?P<subreddit_scope>(.*))/list/?$', ListPostView.as_view(), name='list'),
]
