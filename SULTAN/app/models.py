from django.db import models


class data(models.Model):
  date = models.DateField()
  Location = models.CharField(max_length=255)
  salary = models.IntegerField()
  description = models.CharField(max_length=255)
  




  def __str__(self):
    return f'{self.pk}  .  {self.description} {self.Location}'