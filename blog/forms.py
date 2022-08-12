from django import forms

class CommentForm(forms.Form)
    author = forms.Charfield(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.Charfield(widget=forms.Textarea(
        attrs={
            "class": "form-control"
            "placeholder": "Leave a comment!"
        })
    )