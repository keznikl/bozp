
from django.db.models import Count, Manager

from mezzanine.conf import settings
from mezzanine.core.managers import DisplayableManager


class NewsPostManager(DisplayableManager):
    """
    Extends ``DisplayableManager.published`` with annotated comment counts.
    """

    def published(self, *args, **kwargs):
        return super(NewsPostManager, self).published(*args, **kwargs)

