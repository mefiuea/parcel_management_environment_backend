from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

# validators
package_size_validator = RegexValidator(regex=r'(\d+(,\d+)?)x(\d+(,\d+)?)x(\d+(,\d+)?)',
                                        message='Correct value: A,AxB,BxC,C')


class Parcel(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False)
    contents = models.TextField(blank=False, validators=[MaxLengthValidator(1500)])
    size = models.CharField(max_length=50, blank=True, validators=[package_size_validator])
    weight = models.PositiveIntegerField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return f'Parcel: {self.code}, {self.owner}, {self.name}'


class ParcelShelf(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    parcels = models.ManyToManyField('Parcel', blank=True, related_name='shelf_parcel')

    def __str__(self):
        return f'ParcelShelf: {self.owner}, {self.name}'
