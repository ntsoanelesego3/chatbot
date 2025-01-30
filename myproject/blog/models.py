from django.db import models

# Create your models here.
class user_login(models.Model):
    fname = models.CharField(max_length=50)
    passwd2 = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ''+ self.passwd2
    

class user_register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)


    def __str__(self):
        return self.fname + '' + self.lname + ''+ self.email + '' + self.passwd
    
