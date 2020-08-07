from django.db import models


class Mpesa(models.Model):
    phone_number = models.IntegerField()
    amount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=100,unique=True)

    class Meta:
        ordering = ['-amount']
    
    def __str__(self):
        return str(self.phone_number) + str(self.amount)