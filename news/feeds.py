
from django.contrib.syndication.feeds import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed
from django.utils.html import strip_tags

from news.models import NewsPost, NewsCategory
from news.views import news_page


class PostsRSS(Feed):
    """
    RSS feed for all news posts.
    """
    
    def title(self):
        return news_page().title

    def description(self):
        return strip_tags(news_page().description)

    def link(self):
        return reverse("news_post_feed", kwargs={"url": "rss"})

    def items(self):
        return NewsPost.objects.published().select_related("user")
    
    def categories(self):
        return NewsCategory.objects.all()

    def item_author_name(self, item):
        return item.user.get_full_name() or item.user.username

    def item_author_link(self, item):
        username = item.user.username
        return reverse("news_post_list_author", kwargs={"username": username})

    def item_pubdate(self, item):
        return item.publish_date

    def item_categories(self, item):
        return item.categories.all()


class PostsAtom(PostsRSS):
    """
    Atom feed for all news posts.
    """

    feed_type = Atom1Feed

    def subtitle(self):
        return self.description()

    def link(self):
        return reverse("news_post_feed", kwargs={"url": "atom"})
