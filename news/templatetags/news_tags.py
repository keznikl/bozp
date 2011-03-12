from django.core.exceptions import ObjectDoesNotExist
from news.forms import NewsPostForm
from news.models import NewsPost
from mezzanine import template


register = template.Library()


@register.as_tag
def news_recent_posts(limit=5):
    """
    Put a list of recently published news posts into the template context.
    """
    return list(NewsPost.objects.published()[:limit])


@register.inclusion_tag("admin/includes/quick_news.html", takes_context=True)
def quick_news(context):
    """
    Admin dashboard tag for the quick news form.
    """
    context["form"] = NewsPostForm()
    return context


@register.inclusion_tag("news/latest_news.html", takes_context=True)
def latest_news(context):
    """
    Admin dashboard tag for the quick news form.
    """
    try:
        context["news_post"] = NewsPost.objects.published().latest('publish_date')
    except ObjectDoesNotExist:
        pass
    return context


DISQUS_FORUM_ID = None

