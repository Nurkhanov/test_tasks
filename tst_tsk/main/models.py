from django.db import models
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError


# Create your models here.
class Position(models.Model):
    pos_id = models.BigAutoField(primary_key = True)
    pos_name = models.CharField(max_length=80)
    level = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.pos_name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Boss(models.Model):
    boss_id = models.BigAutoField(primary_key=True)
    boss_position = models.ForeignKey(Position, null=True, on_delete = CASCADE)
    subordinates = models.ManyToManyField(Position,related_name='bosses')

    def __str__(self) -> str:
        return self.boss_position.pos_name

    @property
    def position(self):
        return self.boss_position

    def clean(self) -> None:
        subordinates_list = self.subordinates.objects.all()
        if self.boss_position in subordinates_list:
            raise ValidationError(('Boss cant be in his subordinate list'))


    class Meta:
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'


class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position,on_delete=CASCADE) ###-------------------------
    salary = models.IntegerField(null = False)
    hire_date = models.DateField(null= False) ###-------------------------
    boss = models.ForeignKey(Boss,on_delete=CASCADE)
            
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'




    