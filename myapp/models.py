from ast import Delete
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Neighborhood(models.Model):
    '''
    class for neighbourhods in the app
    '''
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=250)
    admin = models.OneToOneField(User,on_delete=models.CASCADE)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls):
        pass

    @classmethod
    def update_neighborhood(cls):
        pass

    @classmethod
    def update_occupants(cls):
        pass

    def __str__(self):
         return self.name
     
class Profile(models.Model):
    '''
    class for user profiles
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    profile_pic = CloudinaryField('image')
    email = models.EmailField()
    bio = models.TextField(blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)

    
    def __str__(self):
        return f'{self.user.username} profile'
    @receiver(post_save,sender=User) 
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User) 
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    
class Stories(models.Model):
    '''
    class for stories in neighbourhood
    '''
    category = models.CharField(max_length=30)
    #headline = models.TextField(max_length=255)
    headline = models.CharField(max_length=150)
    story = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    def save_stories(self):
        self.save()
        
    def delete_stories(self):
        self.delete()
    
    def __str__(self):
        return f'{self.category} story from {self.neighborhood.name} Neighborhood'
    
    
class Business(models.Model):
    '''
    Model for business class in neighbourhood
    '''
    business_name = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    business_email = models.EmailField()
    business_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = Business.objects.get(business_name__icontains=search_term)
        return business

    def update_business(self):
        self.save()



    # def save_business(self):
    #     self.save()
        
    # def delete_business(self):
    #     self.delete()

    # @classmethod
    # def business_search(cls,search_term):
    #     return cls.objects.filter(business_name__icontains=search_term)

    # def __str__(self):
    #     return f'Business {self.business_name} Owned by {self.user.username}'

class Neighborhood_contact(models.Model):
    '''
    Information for public departmant contacts
    '''
    department = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    contact_email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.department} department contact from {self.neighborhood.name} Neighborhood'

class Announcement(models.Model):
    '''
    Announcements model
    '''
    title = models.CharField(max_length=30)
    announcement = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Announcement for {self.neighborhood.name} Neighborhood' 

