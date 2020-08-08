from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Posts(models.Model):
    country = models.CharField(max_length = 20)
    profession = models.CharField(max_length = 500)
    hobbies = models.TextField(max_length = 500)
    title = models.CharField(max_length=100, default = '')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now)
    content = models.TextField(max_length = 500,default = '')



    def __str__(self):
        return self.title

# to tell django to find the particular path to any specific instance of a post we use get absolutr
#reverse will return the url to be routed as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
