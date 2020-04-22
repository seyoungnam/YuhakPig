from django.db import models
from django.conf import settings
from django.utils import timezone

class GmatModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)

    SUB_CHOICES = (
        ('1', 'Quant'),
        ('2', 'Verbal'),
        ('3', 'IR'),
        ('4', 'AWA')
    )
    subject = models.CharField(max_length=30, choices=SUB_CHOICES)
    file = models.FileField(null=True, upload_to='gmat/%Y/%m%d/') # file will be saved to MEDIA_ROOT/gmat/2015/0130
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


