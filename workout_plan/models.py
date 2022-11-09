from django.db import models
from users import models as userModels

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
    video = models.CharField(max_length= 500)

    def __str__(self):
        return str(self.name)                 


# Wokrout-plan Information Model 
class WorkoutPlanInfo(models.Model):
  user = models.ForeignKey(
          userModels.MyUser, 
          on_delete=models.CASCADE
  )
  height = models.FloatField(max_length=100),
  weight = models.FloatField(max_length=100),
  goal = models.CharField(max_length=100),
  fitnessLevel = models.CharField(max_length=100),
  trainingLevel = models.CharField(max_length=100),
  equipments = models.ManyToManyField(Equipment),
  disablities = models.ManyToManyField(Disability),
  date = models.DateField(auto_now_add=True)
  
  def __str__(self):
        return str(self.user, self.height, self.width, self.goal, self.equipments, self.fitnessLevel, self.trainingLevel,self.disablities, self.date)


 
# Workout plan Model 
class WorkoutPlan(models.Model):
    workoutPlanInfoId = models.OneToOneField(
        WorkoutPlanInfo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    exercies = models.ManyToManyField(Exercise)

    def __str__(self):
        return str(self.workoutPlanInfoId, self.exercies)        


