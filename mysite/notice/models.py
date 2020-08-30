from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Notice(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    message = models.TextField(_("Message"))
    pub_date = models.DateTimeField(_('Message date'), default=timezone.now)
    image = models.FileField(upload_to='notice/media/', blank=True, null=True)

    class Meta:
        ordering = ['pub_date']

    # def __str__(self):
    #     return self.notice
