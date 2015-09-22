from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=5000)
