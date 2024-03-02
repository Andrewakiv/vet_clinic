from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comm_content']
        widgets = {
            'comm_content': forms.Textarea(attrs={'cols': 10, 'rows': 1, 'class': 'contacts-form__input-response',
                                                  'placeholder': "Enter your response"})
        }
