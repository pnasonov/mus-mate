from django import forms

from forum.models import Commentary, Post, Song, Playlist, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        labels = {"title": "Post title", "content": ""}
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Write text of post here..."}
            ),
        }


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


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("title", "artist")
        labels = {"title": "Song name", "content": ""}


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ("name", "description", "songs")
        labels = {
            "name": "Playlist name",
            "description": "Description",
            "songs": "Songs",
        }

    def __init__(self, *args, user=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if user:
            self.fields["songs"] = forms.ModelMultipleChoiceField(
                queryset=Song.objects.filter(owner=user),
                widget=forms.CheckboxSelectMultiple,
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "about_me", "email", "instagram")
        labels = {"instagram": "Instagram (write your instagram name without '@')"}
        widgets = {
            "about_me": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Write something..."}
            ),
        }


class PostSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class SongSearchForm(forms.Form):
    artist = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by artist"}),
    )


class PlaylistSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by playlist name"}
        ),
    )
