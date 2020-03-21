from django import forms
from project.models import Topic


class TopicForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Topic model. """
        model = Topic
        fields = ("title", "content", "author")
