from django.db import models # type: ignore

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"{self.name}, {self.date}, {self.time}, {self.description}"
