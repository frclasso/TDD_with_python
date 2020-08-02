from __future__ import unicode_literals

from django.db import models

class Item(models.Model):

    text = models.TextField(null=True)
