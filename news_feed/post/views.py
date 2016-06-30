import logging
logger = logging.getLogger(__name__)

from django.http import JsonResponse
from django.views.generic.base import View

from .models import Post


class ListPostView(View):

    """
    This view lists all Posts for a given Subreddit.

    Input: a keyword parameter subreddit ID, or the special term 'global' to signify all posts
    Output: 200 on success and a list of dictionaries, each one containing 'id', 'created',
    'title', and 'content'
    """

    def get(self, request, subreddit_scope, *args, **kwargs):
        assert subreddit_scope == 'global'
        posts = Post.objects.all()
        return JsonResponse(
            status=200,
            data={
                'status': 'OK',
                # STUDENT TODO | Return title and content as well
                'posts': [
                    {
                        'id': post.id,
                        'created': post.created,
                    } for post in posts
                ]
            }
        )
