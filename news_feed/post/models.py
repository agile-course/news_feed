from __future__ import unicode_literals

from django.db import models


class Post(models.Model):

    class Meta:
        ordering = ('-created', )

    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    subreddit = models.ForeignKey('subreddit.Subreddit', related_name='posts', null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.title)
