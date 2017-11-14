from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from website.validators import *
from website.paths import *


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[min_length, deny_href])
    doc = models.FileField(upload_to=url_docs, validators=[validate_file_extension])
    date = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return str(self.id) + " | Category ID: " + str(self.category.id) + " | Title: " + self.title
