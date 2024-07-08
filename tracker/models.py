from django.db import models


class Category(models.Model):
    """
  Model representing a financial category for transactions.
  """
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
  Model representing a financial transaction.
  """
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.date} - {self.amount} ({self.category.name})"
