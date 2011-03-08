from django.db import models
from mezzanine.pages.models import Page

# The members of Page will be inherited by the Gallery model, such as
# title, slug, etc. In this example the Gallery model is essentially a
# container for GalleryImage instances.
class Gallery(Page):
    notes = models.TextField("Notes")

class GalleryImage(models.Model):
    gallery = models.ForeignKey("Gallery")
    image = models.ImageField(upload_to="galleries")