from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from mezzanine.conf import settings
from mezzanine.pages.models import ContentPage
from mezzanine.template.loader import select_template
from mezzanine.utils.views import paginate, render_to_response
from news.models import NewsPost


def news_page():
    """
    Return the news page from the pages app.
    """
    try:
        return ContentPage.objects.get(slug=settings.NEWS_SLUG)
    except ContentPage.DoesNotExist:
        return None


def news_post_list(request, template="news/news_post_list.html"):
    """
    Display a list of news posts.
    """
    settings.use_editable()
    news_posts = NewsPost.objects.published(for_user=request.user)
    author = None
    news_posts = paginate(news_posts, request.GET.get("page", 1),
        settings.NEWS_POST_PER_PAGE,
        settings.NEWS_POST_MAX_PAGING_LINKS)
    context = {"news_posts": news_posts, "news_page": news_page()}
    return render_to_response(template, context, RequestContext(request))


def news_post_detail(request, slug, template="news/news_post_detail.html"):
    """
    Display a news post.
    """
    news_posts = NewsPost.objects.published(for_user=request.user)
    news_post = get_object_or_404(news_posts, slug=slug)
    settings.use_editable()
    context = {"news_post": news_post, "news_page": news_page(),}
    request_context = RequestContext(request, context)
    t = select_template(["news/%s.html" % slug, template], request_context)
    return HttpResponse(t.render(request_context))
