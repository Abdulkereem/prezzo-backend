from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Blog

class BlogPostForm(forms.ModelForm):
    article = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'article','banner','uuid']




