
from django.conf.urls.defaults import *

from mezzanine.blog.feeds import PostsRSS, PostsAtom


# Blog feed patterns.
news_feed_dict = {"rss": PostsRSS, "atom": PostsAtom}
urlpatterns = patterns("",
    url("^feeds/(?P<url>.*)/$", "django.contrib.syndication.views.feed",
        {"feed_dict": news_feed_dict}, name="news_post_feed"),
)

# news patterns.
urlpatterns += patterns("news.views",
    url("^(?P<slug>.*)/$", "news_post_detail", name="news_post_detail"),
    url("^$", "news_post_list", name="news_post_list"),
)
