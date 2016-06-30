from django.conf.urls import url

from .views import ListPostView


urlpatterns = [
    url(r'(?P<subreddit_scope>(.*))/list/?$', ListPostView.as_view(), name='list'),
]
