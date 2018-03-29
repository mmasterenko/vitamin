from django.db import models


class Vitamin(models.Model):
    title = models.CharField(max_length=64)
    code = models.CharField(max_length=9, blank=True)
    description = models.TextField(blank=True)
    rdi = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.code if self.code else self.title


class Product(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class VitaminInProduct(models.Model):
    VP_UNITS = (
        ('mkg', 'мкг'),
        ('mg', 'мг'),
        ('g', 'г'),
        ('kg', 'кг'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vitamin = models.ForeignKey(Vitamin, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=3, choices=VP_UNITS)

    def __str__(self):
        return 'vp_{}'.format(self.id)
