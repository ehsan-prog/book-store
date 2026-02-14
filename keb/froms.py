from django import forms 

from .models import Comment,Kteb

class FormComment(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ["text","توصیه_میکنی_یا_نه"]

class FormKteb(forms.ModelForm):
    class Meta:
        model = Kteb
        fields = ["title","author","touzihat","price","cover"]