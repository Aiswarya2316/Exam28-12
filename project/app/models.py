from django.db import models
from django.contrib.auth.models import User

class Mydetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Mydetails')
    age = models.IntegerField()
    phonenumber = models.IntegerField()
    location = models.TextField()
    file = models.FileField(upload_to='Mydetails/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location
