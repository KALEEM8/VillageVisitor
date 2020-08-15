from django.db import models


class Villages(models.Model):
	Name_of_mandal=models.CharField(max_length=100)
	Name_of_village=models.CharField(max_length=100)


class VisitedData(models.Model):
	date=models.CharField(max_length=100)
	participated_by=models.TextField()
	program=models.TextField()
	village_ID=models.ForeignKey(Villages,on_delete=models.CASCADE)
