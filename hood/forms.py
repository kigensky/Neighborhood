from django.forms import ModelForm, HiddenInput
from .models import Mtaa, Post, Business, Essential


class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['creator', 'mtaa', 'timestamp']


class BusinessCreateForm(ModelForm):

    class Meta:
        model = Business
        exclude = ['owner', 'mtaa', 'timestamp']


class EssentialCreateForm(ModelForm):

    class Meta:
        model = Essential
        exclude = ['timestamp']


class MtaaCreateForm(ModelForm):

    class Meta:
        model = Mtaa
        exclude = ['timestamp']