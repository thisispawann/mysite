from django import forms
from .models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        #widgets allows us to formatting builtin bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class':'col-sm-12 form-control'}),
            'email': forms.EmailInput(attrs={'class':'col-sm-12 form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }

