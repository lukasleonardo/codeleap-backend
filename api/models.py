from django.db import models
#from django.utils import timezone

class Post(models.Model):
  username=models.CharField(max_length=50, unique=True,default=' ')
  created_datetime=models.DateField(auto_now_add=True)
  title= models.CharField(max_length=50,default=' ')
  content= models.TextField(default=' ')
  
  def __str__ (self):
    obj = {
        self.username,
        self.created_datetime,
        self.title,
        self.content
        }
    return str(obj)
      
    