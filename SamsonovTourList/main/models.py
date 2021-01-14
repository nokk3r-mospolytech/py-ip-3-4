from django.db import models

# Create your models here.


class TaskDate(models.Model):
    dateIn = models.DateField("Дата отправления")
    dateOut = models.DateField("Дата заключения")

    def __str__(self):
        return str(self.dateIn)

    class Meta:
        verbose_name = 'Даты путешествия'
        verbose_name_plural = 'Даты путешествия'


class TaskTime(models.Model):
    timeIn = models.TimeField("Время отправления")
    timeOut = models.TimeField("Время заключения")

    def __str__(self):
        return str(self.timeIn)

    class Meta:
        verbose_name = 'Время путешествия'
        verbose_name_plural = 'Время путешествия'


class Priority(models.Model):
    priority = models.CharField("Приоритет", max_length=20)

    def __str__(self):
        return self.priority

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритет'


class Pricing(models.Model):
    price = models.IntegerField("Цена")

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цена'


class ChillVariations(models.Model):
    name = models.CharField("Название", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид путешествия'
        verbose_name_plural = 'Вид путешествия'


class Region(models.Model):
    regionName = models.CharField("Название региона", max_length=40)

    def __str__(self):
        return self.regionName

    class Meta:
        verbose_name = 'Название региона'
        verbose_name_plural = 'Название региона'


class Guide(models.Model):
    name = models.CharField("Имя гида", max_length=25)
    rating = models.IntegerField("Рейтинг гида", default='5')

    Region_id = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Регион'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя гида'
        verbose_name_plural = 'Имя гида'


class RatingPlace(models.Model):
    rating_index = models.IntegerField()

    def __str__(self):
        return str(self.rating_index)

    class Meta:
        verbose_name = 'Рейтинг места'
        verbose_name_plural = 'Рейтинг места'


class Avilable(models.Model):
    isAvilable = models.CharField(max_length=5)

    Region_id = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Регион'
    )

    def __str__(self):
        return str(self.isAvilable)

    class Meta:
        verbose_name = 'Возможно ли приехать'
        verbose_name_plural = 'Возможно ли приехать'


class Task(models.Model):
    title = models.CharField('Название', max_length=30)
    descriptions = models.TextField('Описание')

    Pricing_id = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Цена'
    )

    Region_id = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Регион'
    )

    ChillVariations_id = models.ForeignKey(
        ChillVariations,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Вид путешествия'
    )

    Avilable_id = models.ForeignKey(
        Avilable,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='ID поездки'
    )
    Priority_id = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Приоритет'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список туров'
        verbose_name_plural = 'Список туров'

