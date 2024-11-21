from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key = True)
    heading = models.CharField(max_length=100)
    desc = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.heading
    
