from django.db import models


# Create your models here.

class Discount(models.Model):
    Discount_name = models.CharField(max_length=200, verbose_name='Название скидки')
    Discount_percent = models.IntegerField(verbose_name='скидка в %')

    def __str__(self):
        return self.Discount_name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    Tax_name = models.CharField(max_length=200, verbose_name='Налог')
    Tax_percent = models.IntegerField(verbose_name='Налог в %')

    def __str__(self):
        return self.Tax_name

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Order(models.Model):
    odrer_dt = models.DateTimeField(auto_now=True, verbose_name='дата заказа')
    order_name = models.CharField(max_length=200, verbose_name='имя')
    order_discount = models.ForeignKey(Discount, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Скидка')
    order_tax = models.ForeignKey(Tax, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Налог')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderDetail(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    detail_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    item_binding = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Заявка')
    item_count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Детализация'
        verbose_name_plural = 'Детализация'
