from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, RegexValidator

# validators
package_size_validator = RegexValidator(regex=r'(\d+(,\d+)?)x(\d+(,\d+)?)x(\d+(,\d+)?)')


class Parcel(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    parcel_name = models.CharField(max_length=100, blank=False)
    package_contents = models.TextField(blank=False, validators=[MaxLengthValidator(1500)])
    package_size = models.CharField(max_length=50, blank=True, validators=[package_size_validator])
    contact = models.CharField(max_length=50, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Parcel: {self.owner}, {self.parcel_name}'
