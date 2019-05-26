from django.forms import ModelForm
from django import forms
from chp.models import *

class Acomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Academic Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1530@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Academic",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
        (NOT_VISITED, 'Not Visited'),
        (VISITED, 'Visited'),
        (INPROCESS, 'Inprocess'),
        (COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])


	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']




class Adcomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Administrative Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1512@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Administrative",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])


	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']



class Ccomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Civil Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1531@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Civil",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])

	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']


class Ecomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Electrical Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1518@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Electrical",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])

	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']


class Mcomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Mess Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1559@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Mess",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])

	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']


class Scomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Sports Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1507@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Sports",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])
	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']


class Rcomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Ragging Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1528@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Ragging",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])

	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']


class Rcomplainform(ModelForm):
	
	department_head = forms.CharField(initial = "Ragging Head",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	recepient = forms.CharField(initial = "it1528@cemk.ac.in",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	complain_department = forms.CharField(initial = "Ragging",widget=forms.TextInput(attrs={'readonly':'readonly'}))
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(attrs={'readonly':'readonly'},choices=status), initial=status[0])

	
	class Meta:
		model=Complain
		fields=['complain_user','complain_department','complain_subject','department_head','recepient','complain_description','date_posted','status']

class AdminComplainCheckForm(forms.Form):
	
	ADMINISTRATIVE = 'Administrative'
	ACADEMIC = 'Academic'
	CIVIL = 'Civil'
	ELECTRICAL = 'Electrical'
	MESS = 'Mess'
	SPORTS = 'Sports'
	RAGGING = 'Ragging'
	complain_department = (
        (ADMINISTRATIVE, 'Administrative'),
        (ACADEMIC, 'Academic'),
        (CIVIL, 'Civil'),
        (ELECTRICAL, 'Electrical'),
        (MESS, 'Mess'),
        (SPORTS, 'Sports'),
        (RAGGING, 'Ragging'),) 
	complain_department = forms.CharField(widget=forms.Select(choices=complain_department),)
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(choices=status),)


class StaffComplainCheckForm(forms.Form):
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(choices=status),)


class UserComplainCheckForm(forms.Form):
	NOT_VISITED = 'Not Visited'
	VISITED = 'Visited'
	INPROCESS = 'Inprocess'
	COMPLETED = 'Completed'
	status = (
		(NOT_VISITED, 'Not Visited'),
		(VISITED, 'Visited'),
		(INPROCESS, 'Inprocess'),
		(COMPLETED, 'Completed'),)
	status = forms.CharField(widget=forms.Select(choices=status),)


