from django.shortcuts import render
from hoapp.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
def first(request):
	return render(request,'index.html')
def cont(request):
	return render(request,'contact.html')
def about(request):
	return render(request,'about.html')

def service(request):
	return render(request,'services.html')
def short(request):
	return render(request,'shortcodes.html')
def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		d=regi.objects.all().filter(email=email,password=password)
		if d:
			for x in d: 
				request.session['loginid']=x.id
				c=x.usertype
				if c=="admin":	
					return HttpResponseRedirect('/admin_a/')
				else:
					return HttpResponseRedirect('/cust/')
	return render(request,'login.html')
def registration(request):
	if request.method=='POST':
		name_a=request.POST['name']
		em=request.POST['email']
		ph=request.POST['phone']
		psw=request.POST['password']
		if regi.objects.all().filter(email=em):

			return render(request,'registration.html',{'msg':'Email already exist'})
		else:
			a=regi(name=name_a,email=em,phone=ph,password=psw)
			a.save()

	return render(request,'registration.html')
def admin_a(request):
	if request.session.has_key('loginid'):
		a=regi.objects.all().filter(usertype='customer')
		return render(request,'cust_details.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
def pro(request):
	c=request.session['loginid']
	a=regi.objects.filter(id=c)
	return render(request,'p.html',{'b':a})		
def cust(request):
	if request.session.has_key('loginid'):
		a=rooms.objects.all().filter(room_types='A/C',status='available')
		c=rooms.objects.all().filter(room_types='Non A/C',status='available')
		return render(request,'room.html',{'b':a,'d':c})
	else:
		return HttpResponseRedirect('/login/')
def add_room(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			num=request.POST['r_number']
			t=request.POST['room_types']
			pri=request.POST['price']
			img=request.FILES['img']
			if rooms.objects.all().filter(r_number=num):
				return render(request,'addroom.html',{'msg':'Same room exist'})
			else:
				a=rooms(r_number=num,room_types=t,price=pri,pic=img,status='available')
				a.save()

		return render(request,'addroom.html')
	else:
		return HttpResponseRedirect('/login/')
def details(request):
	if request.session.has_key('loginid'):
		a=rooms.objects.all()
		return render(request,'roomdetails.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')

def single(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			a=rooms.objects.all().filter(id=a)
			return render(request,'single.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
def room(request):
	if request.session.has_key('loginid'):
		a=rooms.objects.all().filter(room_types='A/C',status='available')
		c=rooms.objects.all().filter(room_types='Non A/C',status='available')
		return render(request,'room1.html',{'b':a,'d':c})
	else:
		return HttpResponseRedirect('/login/')
def room1(request):
	if request.session.has_key('loginid'):
		a=rooms.objects.all().filter(room_types='A/C')
		c=rooms.objects.all().filter(room_types='Non A/C')
		return render(request,'room1.html',{'b':a,'d':c})
	else:
		return HttpResponseRedirect('/login/')
def home(request):
	if request.session.has_key('loginid'):
		return render(request,'cust/index1.html')
	else:
		return HttpResponseRedirect('/login/')
def c_about(request):
	if request.session.has_key('loginid'):
		return render(request,'cust/about1.html')
	else:
		return HttpResponseRedirect('/login/')	
def c_service(request):
	if request.session.has_key('loginid'):
		return render(request,'cust/service1.html')
	else:
		return HttpResponseRedirect('/login/')	
def c_contact(request):
	if request.session.has_key('loginid'):
		return render(request,'cust/contact1.html')
	else:
		return HttpResponseRedirect('/login/')
def upd(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			a=rooms.objects.all().filter(id=a)
		return render(request,'update.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
def update(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			num=request.POST['r_number']
			t=request.POST['room_types']
			pri=request.POST['price']
			idd=request.POST['id']
			rooms.objects.all().filter(id=idd).update(r_number=num,room_types=t,price=pri)
		return HttpResponseRedirect('/roomdetails/')
	else:
		return HttpResponseRedirect('/login/')
def remove(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			rooms.objects.filter(id=a).delete()
		return HttpResponseRedirect('/roomdetails/')
	else:
		return HttpResponseRedirect('/login/')
def book(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			c=request.session['loginid']
			a=rooms.objects.all().filter(id=a)
			e=regi.objects.all().filter(id=c)
			return render(request,'book.html',{'b':a,'d':e})
	else:
		return HttpResponseRedirect('/login/')
def out(request):
	if request.session.has_key('loginid'):
		del  request.session['loginid']
	logout(request)
	return HttpResponseRedirect('/login/')
from datetime import datetime
def b_room(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			co=request.POST['count']
			date=request.POST['datein']
			date2=request.POST['dateout']
			n=request.POST['r_number']
			c=request.session['loginid']
			i_d=regi.objects.get(id=c)
			r=rooms.objects.get(r_number=n)
			date_for='%Y-%m-%d'
			aa=datetime.strptime(date,date_for)
			ab=datetime.strptime(date2,date_for)
			ac=ab-aa
			bb=ac.days
			bc=rooms.objects.filter(r_number=n)
			for x in bc:
				price=x.price
			total=int(price)*int(bb)
			print(total)	
			rooms.objects.all().filter(r_number=n).update(status='pending')	
			a=bookon(datein=date,dateout=date2,count=co,i_d=i_d,r_id=r,total=total,status='pending')
			a.save()
			return HttpResponseRedirect('/cust/')
	else:
		return HttpResponseRedirect('/login/')
def status(request):
	if request.session.has_key('loginid'):
		c=request.session['loginid']
		a_list=['pending','booked','paid']
		a=bookon.objects.all().filter(i_d=c,status__in=a_list)
		return render(request,'status.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
def c_book(request):
	if request.session.has_key('loginid'):
		#c=rooms.objects.all().filter(status='pending')
		a_list=['pending','booked','paid']
		a=bookon.objects.all().filter(status__in=a_list)
		
		return render(request,'c_book.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
def approve(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			print(a)
			rooms.objects.filter(id=a).update(status='booked')
			bookon.objects.filter(r_id=a).update(status='booked')
			return HttpResponseRedirect('/c_book/')
	else:
		return HttpResponseRedirect('/login/')	
def remove(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			d=bookon.objects.filter(id=a)
			for x in d:
				e=(x.r_id.id)
			rooms.objects.filter(id=e).update(status='available')
			bookon.objects.filter(id=a).update(status='vacate')
			return HttpResponseRedirect('/c_book/')
	else:
		return HttpResponseRedirect('/login/')		
def bill(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
		#	c=request.session['loginid']
			b=bookon.objects.filter(id=a)
		#e=regi.objects.all().filter(id=c)
			return render(request,'pay.html',{'b':b})
	else:
		return HttpResponseRedirect('/login/')
def payment(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			c=request.session['loginid']
			z=request.POST['n']
			rn=request.POST['rn']
			i_d=regi.objects.get(id=c)
			x=bookon.objects.get(id=z)
			print(x)
			#rooms.objects.filter(r_number=rn).update(status='available')
			bookon.objects.filter(id=z).update(status='paid')
			a=paym(i_d=i_d,r=x,payment='paid')	
			a.save()
			return HttpResponseRedirect('/status/')
	else:
		return HttpResponseRedirect('/login/')
def c_pay(request):
	if request.session.has_key('loginid'):
		a=paym.objects.all().filter(payment='paid')
		return render(request,'c_pay.html',{'b':a})
	else:
		return HttpResponseRedirect('/login/')
