from django.db import models

# Create your models here.


PRODUCT_CATEGORY = (
    ('Honey', 'Honey'),
    ('oil', 'oil'),
    ('ghee','ghee'),
    ('Flour', 'Flour'),
    ('Spices', 'Spices'),
    ('Tea', 'Tea'),
    ('Vinegar', 'Vinegar'),
    ('Health Supplements', 'Health Supplements'),
    ('Dates', 'Dates'),
    ('Monthly Packs', 'Monthly Packs'),
    ('Other', 'Other'),
)


class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=100)
    discounted_price = models.IntegerField(null=True , blank=True)
    brand = models.CharField(max_length=100 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    product_image = models.ImageField(upload_to='product_images')
    category = models.CharField(choices=PRODUCT_CATEGORY ,max_length=100)
