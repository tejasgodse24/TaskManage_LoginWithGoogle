from django.db import models

# Create your models here.



class OAuthCredential(models.Model):
    name = models.CharField(max_length=100)
    domain_name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length = 500)
    client_id = models.CharField(max_length=300, null=True, blank=True)
    client_secret = models.CharField(max_length=300, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name