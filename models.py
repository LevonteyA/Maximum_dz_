from django.db import models

# Create your models here.

#создайм класс с описанием структуры таблицы (наследуемся от класса Model)
class OnlineShop(models.Model):
    #создаём заголовок объявления
    #CharField - набор символов
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    #создаём цену
    #decimal_places - количество знаков после запятой
    price = models.DecimalField("Цена", max_digits=10, decimal_places= 2)
    #создаём возможность торговаться
    #auto_now_add=True дата объявления
    auction = models.BooleanField('Торг', help_text='Отметьте уместен ли торг')
    created_time = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True дата обновления объявления
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"OnlineShop(id={self.pk}, title={self.title}, price={self.price})"