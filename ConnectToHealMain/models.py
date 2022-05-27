from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class BlogModel(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 150)
    date_published = models.DateField();
    blog = models.TextField(default = "")
    cover = models.ImageField(default = 'default.jpg', upload_to = 'blogCovers')
    link = models.URLField(default = "", max_length = 200)
    
    def __str__(self):
        return self.title
    
'''
class DiscussionModel(models.Model):
    info = models.TextField(max_length = 255)
    def _str_(self):
        return DiscussionModel.objects.count() + 1
'''

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
    sessionLink = models.CharField(max_length = 250, default = "#")
    def __str__(self):
           return self.user.username + " - " + self.therapistName
     
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_content = models.CharField(max_length=5000)
    post_id = models.AutoField
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return str(self.user1) + " - " + str(self.post_content) + " - "+str(self.post_id)+ " - "+str(self.timestamp)

class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return str(self.user) + " - " + str(self.reply_content) + " - "+str(self.post) + " - "+str(self.timestamp) 
