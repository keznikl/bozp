# This Python file uses the following encoding: utf-8

from mezzanine.conf import register_setting
from django.utils.translation import  ugettext_lazy as _

register_setting(
    name="FOOTER_MESSAGE",
    label=_("Footer message"),
    description=_("The message shown in the footer."),
    editable=True,
    default=u"Copyright© 2010 - 2011 Jolana Mokošová - bezpečnost práce",
)

register_setting(
    name="HOMEPAGE_SLUG",
    label=_("Homepage Slug"),
    description=_("Slug of the homepage."),
    editable=True,
    default=u"homepage",
)