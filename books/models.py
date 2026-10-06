from django.db import models


class Books(models.Model):
    author = models.CharField(max_length=40, verbose_name='автор книги')
    title = models.CharField(max_length=70, verbose_name='название книги')
    description = models.TextField(verbose_name='описание книги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена книги')
    year = models.IntegerField(verbose_name='год выпуска книги')

    class Meta:
        db_table = 'api_books'
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title