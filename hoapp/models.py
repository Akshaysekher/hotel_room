from django.db import models
class regi(models.Model):
	name=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	phone=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')
	usertype=models.CharField(max_length=100,default='customer')
class rooms(models.Model):
	r_number=models.CharField(max_length=100,default='')
	room_types=models.CharField(max_length=100,default='')
	price=models.CharField(max_length=100,default='')
	pic=models.ImageField(upload_to='pics')
	status=models.CharField(max_length=100,default='')
class bookon(models.Model):
	i_d=models.ForeignKey(regi,on_delete=models.CASCADE)
	r_id=models.ForeignKey(rooms,on_delete=models.CASCADE)
	count=models.CharField(max_length=100,default='')
	datein=models.CharField(max_length=100,default='')
	dateout=models.CharField(max_length=100,default='')
	total=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='')
class paym(models.Model):
	i_d=models.ForeignKey(regi,on_delete=models.CASCADE)
	r=models.ForeignKey(bookon,on_delete=models.CASCADE)
	payment=models.CharField(max_length=100,default='pending')
# Create your models here.
