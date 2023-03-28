from django.db import models

# Create your models here.
class UserMapping(models.Model):
    userName= models.CharField(max_length=50)
    userRole= models.IntegerField()

    def __str__(self):
        return u'{0}'.format(self.userRole)


# class Yarn(models.Model):
#     yarnRecived= models.BooleanField()
#     weightOfYarn= models.BigIntegerField()

#     def __str__(self):
#         return self.title