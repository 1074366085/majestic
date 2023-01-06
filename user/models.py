from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    # user_gender = models.CharField(max_length=5, choices=())
    user_phone = models.CharField(max_length=100)

    def __str__(self):
        return f"userName={self.user_name},userPassword={self.user_password},userEmail={self.user_email},userPhone={self.user_phone}"
