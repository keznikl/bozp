import os
import random
from django.core.exceptions import ObjectDoesNotExist
from filebrowser_safe.functions import get_path
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

def is_regular_file(filename):
    """Does `filename` not end with fb_thumb?
       And does `filename` appear to be an image file?"""
    img_types = [".jpg", ".jpeg", ".png", ".gif"]
    ext = os.path.splitext(filename)[1]
    name = os.path.splitext(filename)[0]
    return (not name.endswith("fb_thumb")) and (ext in img_types)

@register.inclusion_tag("includes/homepage_image.html", takes_context=True)
def homepage_image(context):
    # QUERY / PATH CHECK

    path = settings.HOMEPAGE_IMAGE_DIR
    directory = get_path('')
    if path is None or directory is None:
        raise _('The requested Folder does not exist.')

    abs_path = os.path.join(settings.MEDIA_ROOT, path)
    dir_list = [f for f in os.listdir(abs_path) if is_regular_file(f)]

    print("Dir list: " + dir_list.__str__())
    # TODO get random image
    if len(dir_list) > 0:
        pick = random.choice(dir_list)
        context["image"] =  os.path.join(path, pick)
    return context
