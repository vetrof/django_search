from django.db import models

class Realty (models.Model):
    name = models.CharField(max_length=50)
    adres = models.CharField(max_length=300)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img = models.ImageField(upload_to='img')
    cat = models.ForeignKey('Category_realty', on_delete=models.PROTECT)


class Category_realty(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat
