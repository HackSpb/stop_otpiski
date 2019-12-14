from django.db import models
from django.contrib.gis.db import models as gis_models


class GosOrgan(models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')


class Category(models.Model):
    name = models.CharField(max_length=128)


class Complaint(models.Model):
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    RESOLVED = 'resolved'
    PARTLY_RESOLVED = 'party resolved'
    GOT_ANSWER = 'got answer'
    STATUSES = [
        (ACCEPTED, 'Отправлено'),
        (REJECTED, 'Отказ'),
        (RESOLVED, 'Решено'),
        (PARTLY_RESOLVED, 'Частично решено'),
        (GOT_ANSWER, 'Пришел ответ'),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    category = models.ManyToManyField(Category)
    location = gis_models.PointField()
    status = models.CharField(choices=STATUSES, max_length=64)


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    gosorgan = models.ForeignKey(GosOrgan, on_delete=models.CASCADE, blank=True)
    recipient = models.CharField(max_length=64, blank=True)  # name of mayor, official or head of hospital
    incoming_number = models.CharField(max_length=64, blank=True)
    outgoing_number = models.CharField(max_length=64, blank=True)


class Doc(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
