from django.db import models

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50,null=False)
    category = models.CharField(max_length=50,null=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.pname