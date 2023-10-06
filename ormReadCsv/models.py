# csv_orm_app/models.py
from django.db import models

class CSVRecord(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    # Add other fields that match your CSV columns

    def __str__(self):
        return self.name  # Use a relevant field for string representation
