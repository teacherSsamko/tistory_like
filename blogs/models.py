from django.db import models

from helpers.models import BaseModel
from users.models import User

# Create your models here.


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.title}'
