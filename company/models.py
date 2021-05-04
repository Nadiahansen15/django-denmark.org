from django.db import models
from django.forms import ModelForm

# Create your models here.

class address(models.Model):
    streetName = models.CharField(max_length = 45)
    houseNumber = models.CharField(max_length = 25)
    postalCode = models.CharField(max_length = 4)
    region = models.CharField(max_length = 45)

    def __str__(self):
        return '{} {} {} {}'.format(self.streetName, self.houseNumber, self.postalCode, self.region)

class contactInformation(models.Model):
    phoneNumber = models.CharField(max_length = 11)
    email = models.CharField(max_length = 100)
    mainContact = models.CharField(max_length = 50)

    def __str__(self):
        return '{} {} {}'.format(self.phoneNumber, self.email, self.mainContact)

class company(models.Model):
    companyName = models.CharField(max_length = 145)
    companyAddress = models.ForeignKey(address, on_delete = models.CASCADE)
    description = models.TextField()
    companyContactInformation = models.ForeignKey(contactInformation, on_delete = models.CASCADE)
    websiteURL = models.CharField(max_length = 100)
    relationToDjango = models.TextField()

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.companyName, self.companyAddress, self.description, self.companyContactInformation, self.websiteURL, self.relationToDjango)

class addressForm(ModelForm):
    class Meta:
        model = address
        fields = '__all__'

class contactInformationForm(ModelForm):
    class Meta:
        model = contactInformation
        fields = '__all__'

class companyForm(ModelForm):
    class Meta:
        model = company
        fields = ['companyName', 'companyAddress', 'description', 'companyContactInformation', 'websiteURL', 'relationToDjango']


