from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    '''
    class for neighbourhods in the app
    '''
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=250)
    # occupants_count = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

class Profile(models.Model):
    '''
    class for user profiles
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} profile'