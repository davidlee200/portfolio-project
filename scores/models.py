from django.db import models
from django.db.models import Q,F
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime as date
from django.urls import reverse_lazy

# Create your models here.


class Course_model(models.Model):
    TEES_CHOICES=[('Whites','Whites'),('Blues','Blues')]
    course_played = models.CharField(max_length=50,unique=True)
    # tee = models.CharField(max_length = 10, choices=TEES_CHOICES,default ='Whites')
    Par_1 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_2 = models.IntegerField(default=3,validators=[MinValueValidator(1)])
    Par_3 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_4 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_5 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_6 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_7 = models.IntegerField(default=3,validators=[MinValueValidator(1)])
    Par_8 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_9 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_10 = models.IntegerField(default=3,validators=[MinValueValidator(1)])
    Par_11 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_12 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_13 = models.IntegerField(default=5,validators=[MinValueValidator(1)])
    Par_14 = models.IntegerField(default=6,validators=[MinValueValidator(1)])
    Par_15 = models.IntegerField(default=3,validators=[MinValueValidator(1)])
    Par_16 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_17 = models.IntegerField(default=4,validators=[MinValueValidator(1)])
    Par_18 = models.IntegerField(default=4,validators=[MinValueValidator(1)])

    def __str__(self):
        return (self.course_played)

    def get_absolute_url(self): # new
        # return reverse_lazy('home', args=[str(self.id)])
        return reverse_lazy('home')

    @property
    def par(self):
        par = (self.Par_1+self.Par_2+self.Par_3+self.Par_4+self.Par_5+self.Par_6
              +self.Par_7+self.Par_8+self.Par_9+self.Par_10+self.Par_11+self.Par_12
              +self.Par_13+self.Par_14+self.Par_15+self.Par_16+self.Par_17+self.Par_18)
        return par


    class Meta:
        db_table = 'Course'
class Scores_Out(models.Model):
    TEES_CHOICES=[('Whites','Whites'),('Blues','Blues')]
    COURSE_CHOICES= [('Blarney','Blarney'),('Monkstown','Monkstown')]
    fairway_choices = [('Hit','Hit'),('Left','Left'),('Right','Right')]
    putt_choices = [('1',1),('2',2),('3',3),('4',4),('5',5)]
    # course_played = models.ForeignKey(Course_model, on_delete=models.CASCADE)

    # course_played = models.CharField(max_length = 20, choices=Course_model.course_played.unque, default ='Blarney')
    course_played = models.ForeignKey(Course_model, to_field='course_played',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    # tee = models.ForeignKey(Course_model, to_field='tee',on_delete=models.CASCADE)

    tee = models.CharField(max_length = 10, choices=TEES_CHOICES, default ='Whites')
    hole_1 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 1")
    hole_2 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 2")
    hole_3 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 3")
    hole_4 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 4")
    hole_5 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 5")
    hole_6 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 6")
    hole_7 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 7")
    hole_8 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 8")
    hole_9 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 9")
    hole_10 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 10")
    hole_11 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 11")
    hole_12 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 12")
    hole_13 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 13")
    hole_14 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 14")
    hole_15 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 15")
    hole_16 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 16")
    hole_17 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 17")
    hole_18 = models.IntegerField(default=4,validators=[MinValueValidator(1)],verbose_name="Hole 18")
    fairway = models.CharField(max_length = 20, choices=fairway_choices, default ='Hit')
    green = models.BooleanField(verbose_name="Green Hit",default=True)
    putts = models.CharField(max_length = 20, choices=putt_choices,default ='2',verbose_name="No. Of Putts")
    up_and_down = models.BooleanField(verbose_name="Up and Down",default=False)
    bunker_up_and_down = models.BooleanField(verbose_name=" Bunker Up and Down",default=False)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # def __str__(self):
    #     return (self.course_played)

    @property
    def total(self):
        total = (self.hole_1+self.hole_2+self.hole_3+self.hole_4+self.hole_5+self.hole_6
              +self.hole_7+self.hole_8+self.hole_9+self.hole_10+self.hole_11+self.hole_12
              +self.hole_13+self.hole_14+self.hole_15+self.hole_16+self.hole_17+self.hole_18)
        return total

    def get_absolute_url(self): # new
        # return reverse_lazy('home', args=[str(self.id)])
        return reverse_lazy('home')

    class Meta:
        ordering = ['pub_date']
        db_table = 'Scores'


class long_game_practice(models.Model):
    date_of_practice = models.DateField()
    number_of_balls = models.IntegerField()

    def __str__(self):
        return (self.date)

class short_game_practice(models.Model):
    date = models.DateField()
    minutes = models.IntegerField()

    def __str__(self):
        return (self.date)


class lesson(models.Model):
    date = models.DateField()
    Lesson = models.IntegerField(default=1) # defult 1 to show that there was a lession


    def get_absolute_url(self): # new
            return reverse_lazy('home')
