from django.db import models
from django.contrib.auth.models import User

class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='curriculums', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_curriculums', blank=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    curriculum = models.ForeignKey(Curriculum, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

