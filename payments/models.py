from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='сумма оплаты')

    def __str__(self):
        return f'{self.name} на сумму {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
