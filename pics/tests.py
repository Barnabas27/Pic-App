from django.test import TestCase

from .models import Location,Category,Pic

# Create your tests here.

class LocationTestClass(TestCase):
    
    def setUp(self):
        self.Canada = Location(location = 'Canada')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Canada,Location))
        
    def test_save_method(self):
        self.Canada.save()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)
        
class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.Nature = Category(category = 'Nature')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Nature,Category))
        
    def test_save_method(self):
        self.Nature.save()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)
        
# class PicTestClass(TestCase):
#     def setUp(self):
        
#         self.image = Pic()
