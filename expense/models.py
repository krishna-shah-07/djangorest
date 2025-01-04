from django.db import models

# Create your models here.

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=50, choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Expense')
    date = models.DateField()
    # category = models.CharField(max_length=50)
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'Income':
            self.amount = self.amount
        else:
            self.amount = self.amount * -1
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title