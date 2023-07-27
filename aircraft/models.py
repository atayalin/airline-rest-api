import uuid

from django.db import models

from airline.models import Airline

class Aircraft(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manufacturer_serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    number_of_engines = models.IntegerField()

    def __str__(self):
        return f'{self.id, self.manufacturer_serial_number}, {self.type}, {self.model}, {self.operator_airline}, {self.number_of_engines}'