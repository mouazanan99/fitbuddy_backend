from django.db import models
from users import models as userModels
from django.utils import timezone

# Create your models here.

# Equipments Model 
class Equipment(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return str(self.name)


# Disabilities Model 
class Disability(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return str(self.name)   
  

        
# Exercises Model 
class Exercise(models.Model):
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length= 1000)
    bodyTarget = models.CharField(max_length= 100)
    level = models.CharField(max_length= 100)
    MET = models.IntegerField()
    video = models.CharField(max_length= 500)
    equipments = models.ManyToManyField(Equipment)

    
    def __str__(self):
        return str(self.name, self.description, self.level, self.equipments, self.video, self.MET, self.bodyTarget) 



# Wokrout-plan Information Model 
class WorkoutPlan(models.Model):
    user = models.ForeignKey(
          userModels.MyUser, 
          on_delete=models.CASCADE
     )
    height = models.FloatField(max_length=100, default='160')
    weight = models.FloatField(max_length=100, default='60')
    goal = models.CharField(max_length=100, default='Lose Weight')
    fitnessLevel = models.CharField(max_length=100, default='inactive')
    trainingLevel = models.CharField(max_length=100, default='Inactive')
    equipments = models.ManyToManyField(Equipment, default='None')
    disablities = models.ManyToManyField(Disability, default='None')
    date = models.DateField(default=timezone.now)
    exercies = models.ManyToManyField(Exercise)
  
    def __str__(self):
        return str(self.user, self.height, self.weight, self.goal, self.equipments, self.fitnessLevel, self.trainingLevel,self.disablities, self.date, self.exercies)


# Workout Plan Week
class Week(models.Model):
    workoutPlan = models.ForeignKey(WorkoutPlan, 
          on_delete=models.CASCADE)
    number = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return str(self.workoutPlan, self.number, self.startDate, self.endDate)


# Workout Plan Day
class Day(models.Model):
    workoutPlanWeek = models.ForeignKey(Week, 
          on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    exercises = models.ManyToManyField(Exercise, through='Day_Exercise')
    date = models.DateField()



    def __str__(self):
        return str(self.workoutPlanWeek, self.name, self.date)


# Medium Model between many to many (Wokrout Plan Day and Exercise)
class Day_Exercise(models.Model):
    workoutPlanDay = models.ForeignKey(Day, 
          on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, 
          on_delete=models.CASCADE)
    duration = models.IntegerField()
    numberOfSets = models.IntegerField()
    numberOfReps = models.IntegerField()

    def __str__(self):
        return str(self.workoutPlanDay, self.exercise, self.duration, self.numberOfSets,self.numberOfReps)

""" # Workout Plan Day Exercise Set
class WorkoutPlanDayExercise_Set(models.Model):
    workoutPlanDay_Exercise = models.ForeignKey(WorkoutPlanDay_Exercise)
    setNumber = models.IntegerField()
    duration = models.IntegerField()
    doneReps = models.IntegerField() """

                


