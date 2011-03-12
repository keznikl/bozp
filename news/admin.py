
from copy import deepcopy

from django.contrib import admin

from news.models import NewsPost
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin


newspost_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
newspost_fieldsets[0][1]["fields"].append("abstract")
newspost_fieldsets[0][1]["fields"].append("image")
newspost_fieldsets[0][1]["fields"].append("content")



class NewsPostAdmin(DisplayableAdmin, OwnableAdmin):
    """
    Admin class for news posts.
    """

    fieldsets = newspost_fieldsets
    list_display = ("title", "user", "status", "admin_link")


    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)

admin.site.register(NewsPost, NewsPostAdmin)

