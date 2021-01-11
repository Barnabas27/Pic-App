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
        
    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(image=value)
        
# CHOICES = (
#     ('1','Arts'),
#     ('2','Technology'),
#     ('3','Nature'),
#     ('4','Cities'),
# )
    
class Category(models.Model):
     # will have save,update and delete methods
     
     category = models.CharField(max_length=30)
     
     
     def __str__(self):
        return self.category
    
     def save_category(self):
        self.save()
        
     def delete_category(self):
         self.delete()
         
     @classmethod
     def update_category(cls,id,value):
         cls.objects.filter(id=id).update(image=value)

class Pic(models.Model):
    image = models.ImageField(upload_to = 'allpics/',blank = True,null = True)
    name =  models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod
    def search_by_category(cls,category):
        category = cls.objects.filter(category__category__icontains=category)
        return category
    
    @classmethod
    def filter_by_location(cls,location):
        location = cls.objects.filter(location__location=location).all()
        return location
    
    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)
    class Meta:
        ordering = ['name']
