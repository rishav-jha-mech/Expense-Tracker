from django.db import models

class Expense(models.Model):

    TYPE_CHOICES = (
        ('Me', 'Me'),
        ('Others', 'Others'),
    )
    CATEGORY_CHOICES = (
        ('Food','Food'),
        ('Travel','Travel'),
        ('Shopping','Shopping'),
        ('Education','Education'),
        ('Medical','Medical'),
        ('Entertainment','Entertainment'),
        ('Others','Others'),
    )

    date = models.DateField()
    amount = models.BigIntegerField()
    person = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices= CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.description