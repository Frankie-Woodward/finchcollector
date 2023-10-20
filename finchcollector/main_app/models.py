from django.db import models
# Import the reverse function
from django.urls import reverse
CHARGETIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)
# Create your models here.
class Ev(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    battery_mileage = models.IntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.id})'
      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ev_id': self.id})

class Charging(models.Model):
    date = models.DateField('Charging Date')
    charge = models.CharField(
        max_length=1,
        choices=CHARGETIMES,
        default=CHARGETIMES[0][0]
        )
    # Create an ev_id FK
    ev = models.ForeignKey(
        Ev, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_charge_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

    



# For basic lookups, the format is: field__lookuptype=value (that's a double underscore).