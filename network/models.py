from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    #Контакты
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    #Продукты
    product_name = models.CharField(max_length=200, verbose_name='Название продукта')
    product_model = models.CharField(max_length=200, verbose_name='Модель продукта')
    product_release_date =  models.DateField(verbose_name='Дата выхода продукта')

    #Поставщик
    supplier = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name='Поставщик',
    )

    #Задолженность перед поставщиком
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Задолженность')
    #Время создания
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')\

    def __str__(self):
        return f'{self.name}({self.city})'

class Meta:
    verbose_name = 'Звено сети'
    verbose_name_plural = 'Звенья сети'




