from django.db import models

class Observation(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    radar_image = models.ImageField(upload_to='radar/', null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} | {self.temperature}°C"

