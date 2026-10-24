from django.db import models
from django.utils import timezone

class BasePublishModel(models.Model):
    class ProducStateOptions(models.TextChoices): 
        DRAFT = "BR", "BORRADOR"
        PUBLISHED = "PU", "PUBLICADO" 
        PRIVATE = "PR", "PRIVADO" 

    state = models.CharField(max_length=2, choices=ProducStateOptions.choices, default=ProducStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

    class Meta:
        abstract = True
        ordering = ["-update", "-timestamp"]

    def save(self, *args, **kwargs):
        if self.state_is_published and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        else:
            self.publish_timestamp = None
        super().save(*args, **kwargs)

    @property
    def state_is_published(self):
        return self.state == self.ProducStateOptions.PUBLISHED

    def is_published(self):
        publish_timestamp = self.publish_timestamp
        return self.state_is_published and publish_timestamp < timezone.now()
        