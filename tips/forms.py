from django import forms

from pagedown.widgets import PagedownWidget

from .models import Blog

class BlogForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget)
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Blog
		fields =[
			"title",
			"blog_type",
			"content",
			"image",
			"draft",
			"publish",
		]


