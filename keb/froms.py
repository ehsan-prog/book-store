from django import forms 

from .models import Comment

class FormComment(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ["text","توصیه_میکنی_یا_نه"]
