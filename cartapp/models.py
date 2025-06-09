from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product  # adjust import if needed

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "add_tocart"

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity}"
