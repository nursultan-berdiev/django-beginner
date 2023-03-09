from django.db import models


class TestModel(models.Model):
    string = models.CharField(max_length=20, verbose_name="Название поля 1")
    date = models.DateField(verbose_name="Дата 1")
    datetime = models.DateTimeField(verbose_name="Дата и время")
    checkbox = models.BooleanField(verbose_name="Чек бокс")
    integer = models.IntegerField(verbose_name="Число")
    choices = models.IntegerField(verbose_name='Выборка', choices=(
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
    ))
    nullable = models.TextField(verbose_name="Какой то текст", blank=True, null=True)

    def __str__(self):
        return f"Тестовая Модель №{self.id}"

