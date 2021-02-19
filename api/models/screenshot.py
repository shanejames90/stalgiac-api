from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Screenshot(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=500, blank=True)
  imagefile = models.FileField(upload_to='screenshots/', null=True, verbose_name="")
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    # This must return a string
    return f"The screenshot '{self.title}' {self.imagefile} has description {self.description}."

  def as_dict(self):
    """Returns dictionary version of Screenshot models"""
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'owner': self.owner,
        'imagefile': self.imagefile,
    }
