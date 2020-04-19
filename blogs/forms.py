from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ['user']
        error_messages = {
            'title': {
                'required': "제목을 입력해주세요."
            },
            'content': {
                'required': '내용을 입력해주세요.'
            }
        }
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
