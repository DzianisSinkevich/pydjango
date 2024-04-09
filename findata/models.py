from django.db import models


class FinData(models.Model):
    date = models.DateField('Дата операции')
    value = models.FloatField('Сумма', max_length=10)
    operation = models.CharField('Операция', max_length=10, default='Расход')
    category = models.CharField('Категория', max_length=20)

    def __str__(self) -> str:
        return self.operation

    class Meta:
        verbose_name = 'Фин данные'
        verbose_name_plural = 'Фин данные'


class Category(models.Model):
    rus = models.CharField('Категория RUS', max_length=20)
    eng = models.CharField('Категория ENG', max_length=20)

    def __str__(self) -> str:
        return self.rus

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class FinDataGroup(models.Model):
    category = models.CharField('Категория RUS', max_length=20)
    value = models.FloatField('Сумма', max_length=10)
    operation = models.CharField('Операция', max_length=10)
    date_me = models.CharField('Дата', max_length=20)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name = 'Финдата сгрупп'
        verbose_name_plural = 'Финдата сгрупп'
