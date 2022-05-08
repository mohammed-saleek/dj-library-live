from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length= 100)
    author_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_on = models.DateTimeField(blank=True, null=True)
    Language = models.CharField(max_length=100)
    image = models.ImageField(blank = True, upload_to='images/')
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.book_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " "
        return url
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.email
    
    