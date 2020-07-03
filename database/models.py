from datetime import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=150)
    type = models.CharField('Тип изделия', max_length=150)
    count = models.PositiveSmallIntegerField('Количество', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'


class Contractor(models.Model):
    name = models.CharField('Имя', max_length=150)
    productType = models.ManyToManyField(Product, verbose_name='Тип изделий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Client(models.Model):
    name = models.CharField('Имя клиента', max_length=150)
    typeSells = models.CharField('Тип заказа', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    name = models.CharField('Название', max_length=200, default='Заказ '+str(id), null=True)
    description = models.TextField('Описание')
    productType = models.ManyToManyField(Product, verbose_name='Тип изделия')
    contractor = models.ManyToManyField(Contractor, verbose_name='Поставщик')
    deadline = models.DateField('Дата выполнения заказа', default=datetime.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Service(models.Model):
    description = models.TextField('Содержание')
    serviceType = models.CharField('Услуга', max_length=300)

    def __str__(self):
        return self.serviceType

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Staff(models.Model):
    name = models.CharField('Имя', max_length=150)
    sector = models.CharField('Отдел', max_length=200)
    position = models.CharField('Должность', max_length=150)
    dateOfStartWork = models.DateField('Начало работы', default=datetime.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Cost(models.Model):
    count = models.PositiveSmallIntegerField('Количество', default=0)
    costsType = models.CharField('Тип затрат', max_length=500)

    def __str__(self):
        return self.costsType

    class Meta:
        verbose_name = 'Расчет затрат'
        verbose_name_plural = 'Расчеты затрат'


class Training(models.Model):
    students = models.CharField('Студент', max_length=150)
    sector = models.CharField('Отделение', max_length=300)
    startLearningDate = models.DateField('Начало обучение', default=datetime.today)
    endLearningDate = models.DateField('Конец обучения', default=datetime.today)

    def __str__(self):
        return self.students

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
