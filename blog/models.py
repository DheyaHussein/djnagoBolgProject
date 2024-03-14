from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name




class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blog_posts')

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-publish']
        indexes =[
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})



