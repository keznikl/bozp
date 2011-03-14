"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from bozpsite.templatetags.global_tags import is_regular_file

class SimpleTest(TestCase):
    def test_home_image_valid(self):
        """
        Tests that is_regular_file passes valid name
        """
        self.failUnless(is_regular_file("file.test.png"), "is_regular_file rejected regular file")
    def test_home_image_invalid(self):
        """
        Tests that is_regular_file rejects invalid name
        """
        self.failIf(is_regular_file("file.test_fb_thumb.png"), "is_regular_file accepted invalid file")

__test__ = {"doctest": """
Testing global tags
"""}

