from django.db import models

# Create your models here.

class Products(models.Model):
    Name=models.CharField(max_length=30)
    Weight=models.DecimalField(max_digits=5,decimal_places=2)
    Price=models.DecimalField(max_digits=5,decimal_places=2)
    created_at=models.DateField()
    updated_at=models.DateField()

    def __str__(self):
        return self.Name

    class Meta:
        db_table='db_app1'
