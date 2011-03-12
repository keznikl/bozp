from mezzanine.conf import register_setting
from django.utils.translation import  ugettext_lazy as _



register_setting(
    name="NEWS_SLUG",
    label=_("News slug"),
    description=_("The slug name for page representing the news list."),
    editable=True,
    default='news',
)

register_setting(
    name="NEWS_PER_PAGE",
    label=_("News per page"),
    description=_("The number of news entries to show on a single page."),
    editable=True,
    default=10,
)

register_setting(
    name="NEWS_IMG_DIR",
    label=_("News image directory"),
    description=_("The directory for news images."),
    editable=True,
    default="uploads/news",
)
  