from django.db import models
from usermanage.models import User

class Supplier(models.Model):
    user= models.OneToOneField(User, verbose_name="Employe ID", )
    name=models.CharField(max_length=50, verbose_name="Supplier Name" , default="New Service")
    email=models.EmailField(blank=True)
    image = models.ImageField(verbose_name="Image", null='True', upload_to='img')

    def __str__(self):
        return ("%s" % self.name)

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Service Name",)
    info = models.CharField(max_length=50, verbose_name="Info")
    credit = models.IntegerField(verbose_name="Service Credit")
    image = models.ImageField(verbose_name="Service Photo",upload_to='img')
    supplier = models.ForeignKey(Supplier, verbose_name="Supplier's ID")
    def __str__(self):
        return ("%s"%self.name)
