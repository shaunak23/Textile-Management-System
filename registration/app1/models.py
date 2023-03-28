from django.db import models

# Create your models here.
class UserMapping(models.Model):
    userName= models.CharField(max_length=50)
    userRole= models.IntegerField()

    def __str__(self):
        return u'{0}'.format(self.userRole)

class AdminJobCard(models.Model):
    orderNo= models.AutoField(primary_key=True)
    orderDate= models.DateField()
    companyName= models.CharField(max_length=100)
    gst= models.CharField(max_length=100)
    quality= models.CharField(max_length=100)
    ppc= models.IntegerField()
    rate= models.IntegerField()
    deadline= models.DateField()
    count= models.IntegerField()
    construction= models.IntegerField() #derived field
    lengthOfCloth= models.IntegerField()
    color= models.CharField(max_length=100)
    target= models.CharField(max_length=100, default="None")
    isYarningDone = models.BooleanField(default=False)
    isWindingDone = models.BooleanField(default=False)
    isWarpingDone = models.BooleanField(default=False)
    isLoomingDone = models.BooleanField(default=False)
    isCheckingDone = models.BooleanField(default=False)
    isRepairingDone = models.BooleanField(default=False)

class Yarn(models.Model):
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE, primary_key=True)
    yarnReceived= models.BooleanField()
    weightOfYarn= models.IntegerField()

class Winding(models.Model):
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE, primary_key=True)
    yarnReceived= models.BooleanField()
    noOfCones= models.IntegerField()
    sizeOfCones= models.CharField(max_length=100)
    noOfDoffs= models.IntegerField()
    finalWeightOfCone= models.IntegerField()
    wasteCollectionWeight= models.IntegerField()
    defects= models.CharField(max_length=100, default=None)
    
class Warping(models.Model):
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE,primary_key=True)
    finalWeightOfWarpedYarn= models.IntegerField()
    wasteCollectionWeight= models.IntegerField()
    # buttonToReportToSupervisor= models.CharField(max_length=100)
    packageDefects= models.CharField(max_length=200)

class Looming(models.Model):
    yarnReceived= models.BooleanField()
    date= models.DateField()
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE,primary_key=True)
    loomNo= models.IntegerField()
    totalPicks= models.IntegerField()
    target= models.IntegerField(default=None)
    wasteCollectionWeight= models.IntegerField()
    

class Checking(models.Model):
    date= models.DateField()
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE, primary_key=True)
    loom= models.IntegerField()
    worker= models.CharField(max_length=100)
    defectInMeters= models.IntegerField()
    points= models.CharField(max_length=100)
    grade = models.IntegerField(default=None)
    repairable= models.BooleanField()
    
class Repairing(models.Model):
    date= models.DateField()
    orderNo =models.ForeignKey(AdminJobCard, on_delete=models.CASCADE, primary_key=True, default=None)
    repairingMachine= models.CharField(max_length=100)
    worker= models.CharField(max_length=100)


