from django.db import models

class Product(models.Model):
    GENDER=(
        ('M','M'), #MALE
        ('F','F'), #FEMALE
        ('U','U'), #UNISEX
    )

    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    purchase=models.CharField(max_length=10)
    sale=models.CharField(max_length=10)
    qty=models.CharField(max_length=10)
    gender=models.CharField(max_length=1, null=True, choices=GENDER) 
    note=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        