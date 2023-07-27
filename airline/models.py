from django.db import models

class Airline(models.Model):

    #     "name": "Turkish Airlines",
    #     "callsign": "TURKISH",
    #     "founded_year": 1933,
    #     "base_airport": "IST"

    name = models.CharField(primary_key=True, max_length=100)
    callsign = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.callsign}, {self.founded_year}, {self.base_airport}'
    