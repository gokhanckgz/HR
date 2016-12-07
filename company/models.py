from django.core.validators import RegexValidator
from django.db import models
from usermanage.models import User
from supplier.models import Service
###For Commit###
class Company(models.Model):
    user = models.OneToOneField(User, verbose_name="User ID")
    company_name = models.CharField(max_length=20, verbose_name="Name", default="New User")
    image = models.ImageField(verbose_name="Image", null='True', upload_to='img')

    def __str__(self):
        return str(self.id)

class Employe(models.Model):
    user = models.OneToOneField(User, verbose_name="User ID", )
    name = models.CharField(max_length=20, verbose_name="Name", default="New User")
    surname = models.CharField(max_length=30, verbose_name="Surname")
    image = models.ImageField(verbose_name="Image", null='True', upload_to='img')
    phone_regex = RegexValidator(regex=r'^\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True , max_length=12)  # validators should be a list
    credit = models.IntegerField(verbose_name="Credit", default=0)
    company = models.ForeignKey(Company, verbose_name="Company ID")

    def __str__(self):
        return str(self.id)


class Benefit(models.Model):
    employe = models.ForeignKey(Employe)
    supplier_service = models.ForeignKey(Service)

    def __str__(self):
        return 'Employe ID is %s and Benefit ID is %s' % (str(self.employe_id), str(self.supplier_service_id))

class Company_Service(models.Model):
    company = models.ForeignKey(Company)
    service = models.ForeignKey(Service)
    def __str__(self):
        return str(self.id)