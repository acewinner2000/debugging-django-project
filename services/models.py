from django.db import models

# Create your models here.
class Services(models.Model):
    titel=models.CharField(max_length=50)
    content=models.TextField()
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.titel
    
    class Meta:
        ordering=('created_at',)

# Create your models here.
class Services_a(models.Model):
    titel=models.CharField(max_length=50)
    content=models.TextField()
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.titel
    
    class Meta:
        ordering=('created_at',)