# inventory
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class StockStatus(models.Model):
    """
    Stock status values such as "In Stock", "Backordered", etc.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Stock Status'

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    """
    An inventoried item represented by any Django model by means of the Content
    Types framework.
    """
    sku = models.CharField(max_length=75, unique=True, db_index=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    qty = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50, blank=True, null=True)
    stock_status = models.ForeignKey(StockStatus, db_index=True, on_delete=models.CASCADE)
    stock_comment = models.CharField(max_length=255, blank=True, null=True)

    # def __unicode__(self):
    #     content_type = ContentType.objects.get_for_model(self.content_object)
    #     return str(content_type.get_object_for_this_type(pk=self.object_id))

    def __str__(self):
        # from django.contrib.contenttypes.models import ContentType
        # content_type = ContentType.objects.get_for_model(self.content_object)
        return str(self.sku)


class Transaction(models.Model):
    """
    A transaction which adds or removes items from inventory.
    """
    TYPE_RECIEVED = 1
    TYPE_SOLD = 2
    TYPE_RETURNED = 3
    TYPE_INTERNAL = 4
    TYPE_ADJUSTMENT = 5
    TYPE_PHYSICAL_COUNT = 6
    TYPE_CYCLE_COUNT = 7
    TYPE_SCRAP = 8

    TYPE_CHOICES = (
        (TYPE_RECIEVED, 'Received'),
        (TYPE_SOLD, 'Sold'),
        (TYPE_RETURNED, 'Returned to Stock'),
        (TYPE_INTERNAL, 'Internal Transfer'),
        (TYPE_ADJUSTMENT, 'Adjustment'),
        (TYPE_PHYSICAL_COUNT, 'Physical Count'),
        (TYPE_CYCLE_COUNT, 'Cycle Count'),
        (TYPE_SCRAP, 'Scrapped')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    transaction_type = models.PositiveIntegerField(choices=TYPE_CHOICES, db_index=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    # optional generic relationship to associated object (eg. order, po, etc.)

    content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "%s on %s" % (self.get_transaction_type_display(), str(self.date))


class TransactionItem(models.Model):
    """
    A line item on an inventory transaction.
    """
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
