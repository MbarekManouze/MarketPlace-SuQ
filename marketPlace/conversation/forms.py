from django import forms
from .models import ConversationMessage


INPUT_STYLE = "w-full py-4 px-6 rounded-xl border bg-gray-100 bg-opacity-50"

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_STYLE,
            })
        }