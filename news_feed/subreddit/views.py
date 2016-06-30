import logging
logger = logging.getLogger(__name__)

from django.http import JsonResponse
from django.views.generic.base import View

from .models import Subreddit


class ListSubredditView(View):

    """
    This view lists all Subreddits.

    Output: 200 on success and a list of dictionaries, each one containing 'id', 'created',
    'title', and 'description'
    """

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            status=200,
            data={
                'status': 'OK',
                # STUDENT TODO | Return title and description as well
                'subreddits': [
                    {
                        'id': subreddit.id,
                        'created': subreddit.created,
                    } for subreddit in Subreddit.objects.all()
                ]
            }
        )
