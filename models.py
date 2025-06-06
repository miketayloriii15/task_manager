from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
