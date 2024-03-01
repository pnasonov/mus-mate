from django import forms

from forum.models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Write a comment..."}
            ),
        }


class PostSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
