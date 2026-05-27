from django.db import models

class InletPoint(models.Model):
    pointid = models.IntegerField()
    name = models.CharField(max_length = 255, blank = True)
    status = models.CharField(max_length = 255, blank = True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
