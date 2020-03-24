from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Represents a single TOPICS Topic. """
    title = models.CharField(max_length=settings.PROJECT_TOPIC_TITLE_MAX_LENGTH, unique=True,
                             help_text="Title of your Topic.")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="The user that posted this article.")
    slug = models.CharField(max_length=settings.PROJECT_TOPIC_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this Topic. Generated by the system.")
    content = models.TextField(
        help_text="Write the content of your Topic here.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this Topic was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this Topic was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a Topic (/my-new-TOPICS-Topic). """
        path_components = {'slug': self.slug}
        return reverse('topic-details-project', kwargs=path_components)
        # return reverse('topics:topics-update-Topic', kwargs=path_components)
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a Topic is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Topic, self).save(*args, **kwargs)

class Food(models.Model):
    title = models.CharField(max_length=settings.PROJECT_TOPIC_TITLE_MAX_LENGTH, unique=True,
                            help_text="Title of your Topic.")
    image = models.ImageField(upload_to='images/')
    ingredients = models.TextField(
        help_text="Write the engredients of your Food here.")
