from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Theme(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='theme/')
    summary = models.TextField()
    numPeople = models.IntegerField()
    difficulty = models.IntegerField()
    activity = models.IntegerField()
    genre = models.CharField(max_length=20)
    horror = models.IntegerField()
    time1 = models.CharField(max_length=10)
    time2 = models.CharField(max_length=10)
    time3 = models.CharField(max_length=10)
    time4 = models.CharField(max_length=10)
    time5 = models.CharField(max_length=10)
    time6 = models.CharField(max_length=10)
    time7 = models.CharField(max_length=10)
    time8 = models.CharField(max_length=10)
    time9 = models.CharField(max_length=10)
    time10 = models.CharField(max_length=10)

    def __str__(self):
        return self.name

Way = (
    ('현장결제', '현장결제'),
    ('무통장선결제', '무통장선결제'),
)

Num = (
    ('1명', '1명'),
    ('2명', '2명'),
    ('3명', '3명'),
    ('4명', '4명'),
    ('5명', '5명'),
    ('6명', '6명'),
)

class Booking(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    numPeople = models.CharField(max_length=20, choices=Num)
    depositWay = models.CharField(max_length=20, choices=Way)


