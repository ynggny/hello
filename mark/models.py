from django.db import models
from django.core import validators

class Stu(models.Model):
    grade = (
    (1,'中1'),
    (2,'中2'),
    (3,'中3'),
    (4,'高1'),
    (5,'高2'),
    (6,'高3'),
    (7,'講師'),
    )

    name = models.CharField(
    verbose_name='名前',
    max_length=200,
    )
    age=models.IntegerField(
    verbose_name='学年',
    choices=grade,
    default=1
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'


# Create your models here.
