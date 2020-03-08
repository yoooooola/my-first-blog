from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Post is name of class(object), first character should be always upper case
# models mean Post is model of Django

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # if the text length is limited then we can use models.CharField
    text = models.TextField() # if the text length is unlimited
    created_date = models.DateTimeField( # date and time
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # models.ForeignKey : link for another model

    def publish(self): # method, publish is name for name we can use lower case and _
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
