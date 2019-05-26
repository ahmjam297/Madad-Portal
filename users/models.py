from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	UID =models.CharField(max_length=30,default = "000",help_text = "'Staff's fill their STAFF ID and student's fill their ROLL NO " )
	MALE = 'M'
	FEMALE = 'F'
	Gender=((MALE, 'Male'),(FEMALE, 'Female'),)
	Gender=models.CharField(max_length=6,choices=Gender,default=MALE,)
	FIRST = '1st'
	SECOND = '2nd'
	THIRD = '3rd'
	FOURTH = '4th'
	NGH = 'NGH'
	NON_HOSTELER = 'Non_hosteler'
	TEACHER_QUARTER = 'Teacher_quarter'
	residence = ((FIRST, 'First'),(SECOND, 'Second'),(THIRD, 'Third'),(FOURTH, 'Fourth'),(NGH,'NGH'),(NON_HOSTELER, 'Non_hosteler'),(TEACHER_QUARTER,'Teacher_quarter'))
	residence = models.CharField(max_length=20,choices=residence,default=FIRST,)
	room_no=models.CharField(max_length=10,default = "000")

	def __str__(self):
		return f'{self.user.username} Profile'

