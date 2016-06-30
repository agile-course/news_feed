import json
import logging
logger = logging.getLogger(__name__)

from django.http import JsonResponse
from django.views.generic.base import View

from .models import Subreddit


class CreateSubredditView(View):

    """
    This view creates a Subreddit object.

    Input: input_data, a json string representing a dictionary containing
    'title' and 'description' keys.

    Output: 200 on success, 400 on missing parameter
    """

    def post(self, request, *args, **kwargs):
        input_data = json.loads(request.body)

        if 'title' not in input_data or 'description' not in input_data:
            logger.error('Missing parameter')
            return JsonResponse(status=400, data={'status': 'Missing parameter'}, safe=False)

        # STUDENT TODO | Create subreddit from parameters

        return JsonResponse(status=200, data={'status': 'OK'}, safe=False)


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
