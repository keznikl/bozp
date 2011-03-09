from django.db import models
from django.utils.translation import  ugettext_lazy as _

from mezzanine.core.models import Displayable, Ownable, Content
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

