
from django import forms

from news.models import NewsPost



class NewsPostForm(forms.ModelForm):
    """
    Model form for ``NewsPost`` that provides the quick blog panel in the
    admin dashboard.
    """

    class Meta:
        model = NewsPost
        fields = ("title", "abstract", "content", "status")

    def __init__(self):
        super(NewsPostForm, self).__init__()
        self.fields["status"].widget = forms.HiddenInput()
