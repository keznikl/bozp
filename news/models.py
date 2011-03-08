
from datetime import datetime
from hashlib import md5

from django.db import models
from django.template.defaultfilters import truncatewords_html
from django.utils.translation import ugettext, ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.models import Displayable, Ownable, Content, Slugged
from news.managers import NewsPostManager


class NewsPost(Displayable, Ownable, Content):
    """
    A news post.
    """

    objects = NewsPostManager()

    class Meta:
        verbose_name = _("News post")
        verbose_name_plural = _("News posts")
        ordering = ("-publish_date",)

    @models.permalink
    def get_absolute_url(self):
        return ("news_post_detail", (), {"slug": self.slug})

