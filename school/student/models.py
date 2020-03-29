from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Student(models.Model):
    enroll_num = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=120)
    class_room = models.ForeignKey('ClassRoom', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + "-" + str(self.enroll_num)


class ClassRoom(models.Model):
    type = models.CharField(max_length=40)
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12),])

    def __str__(self):
        return str(self.grade) + " " + str(self.    type)
