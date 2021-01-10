from django.db import models

# Create your models here.

class Location(models.Model):
    # will have save,update and delete methods
    location = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
class Category(models.Model):
     # will have save,update and delete methods
     category = models.CharField(max_length = 100)
     
     def __str__(self):
        return self.category
    
     def save_category(self):
        self.save()
        
     def delete_category(self):
         self.delete()

class Pic(models.Model):
    image = models.ImageField(upload_to = 'allpics/',blank = True)
    name =  models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    

