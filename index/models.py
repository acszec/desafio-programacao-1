from django.db import models


class Report(models.Model):
    purchaser_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_price = models.FloatField()
    purchase_count = models.IntegerField()
    merchant_address = models.CharField(max_length=100)
    merchant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_description
