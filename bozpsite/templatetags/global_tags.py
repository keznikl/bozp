from django.core.exceptions import ObjectDoesNotExist
from mezzanine import template
from mezzanine.conf import settings
from mezzanine.pages.models import ContentPage


register = template.Library()

@register.simple_tag
def footer_text():
    """
    Return the footer text
    """
    return settings.FOOTER_MESSAGE

@register.inclusion_tag("includes/homepage.html", takes_context=True)
def get_homepage(context):
    """
    Retrive the home page text
    """
    slug = settings.HOMEPAGE_SLUG
    try:
        context["homepage"] = ContentPage.objects.published().get(slug=slug)
    except ObjectDoesNotExist:
        pass
    return context


