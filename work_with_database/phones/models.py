from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    release_date = models.DateField()
    lte_exists =models.BooleanField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return f"{self.id}:{self.name}"
