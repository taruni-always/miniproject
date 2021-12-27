from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 150)
    date_published = models.DateField();
    blog = models.TextField(default = "")
    cover = models.ImageField(default = 'default.jpg', upload_to = 'blogCovers')
    link = models.URLField(default = "", max_length = 200)
    
    def __str__(self):
        return self.title
    
class DiscussionModel(models.Model):
    info = models.TextField(max_length = 255)
    def _str_(self):
        return DiscussionModel.objects.count() + 1

class TherapistModel(models.Model):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    aboutMe = models.CharField(max_length = 1024)
    workExperience = models.CharField(max_length = 1024)
    pricePerSession = models.IntegerField()
    cover = models.ImageField(default = 'default.jpg', upload_to = 'profilephotos')
    
    def __str__(self):
       return self.username
   
class BookAppointmentModel(models.Model):
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    user = models.ForeignKey(User, related_name="appointment_user", on_delete=models.CASCADE, null=True)
    therapistName = models.CharField(max_length = 50, blank = True, null = True, unique = False)
    date = models.DateField()
    fromTime = models.TimeField()
    toTime = models.TimeField()
    sessionstatus = models.BooleanField(default=False)
    
    def __str__(self):
           return self.user.username + " - " + self.therapistName
     