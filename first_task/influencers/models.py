from django.db import models

class Data(models.Model):
    username = models.CharField(max_length=250, default='')
    followerCount = models.CharField(max_length=500, default='0')
    avgLikesRatio = models.CharField(max_length=500, default='0')
    avgCommentsRatio = models.CharField(max_length=500, default='0')
    picture = models.CharField(max_length=100000, null=True)

    def __str__(self):
        return self.username