from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    description = models.TextField()


    def __str__(self): # pylint: disable=invalid-str-returned
        return self.name

    def get_absolute_url(self):
        return reverse('content:course-detail', kwargs={'slug': self.slug})


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self): # pylint: disable=invalid-str-returned
        return self.title

    def get_absolute_url(self):
        return reverse('content:video-detail', kwargs={
            'video_slug': self.slug, 
            'slug': self.course.slug # pylint: disable=maybe-no-member
        })

def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_course, sender=Course)
pre_save.connect(pre_save_video, sender=Video)