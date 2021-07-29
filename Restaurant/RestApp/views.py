from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,Rlupd
from RestApp.models import Restaurant,Rolereq,User
from RestApp.models import Item
from RestApp.forms import ItemForm,Chgepwd,Pfupd
#from RestApp.forms import Profile
from django.contrib import messages
from RestApp.forms import UsgForm,Rltype
from django.contrib.auth.decorators import login_required
#EMAIL concept
from Restaurant import settings
from django.core.mail import send_mail
  
# Create your views here.
def home(request):
	alldata=Restaurant.objects.filter(uid_id=request.user.id)
	t=Restaurant.objects.all()
	return render(request,'app/home.html',{'alldata':alldata,'y':t})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

def login(request):
	return render(request,'app/login.html')

@login_required
def restlist(request):
	alldata=Restaurant.objects.filter(uid_id=request.user.id)
	if request.method=="POST":
		t=ReForm(request.POST,request.FILES)
		#print(t) for debug purpose
		if t.is_valid():  #Django validation
			c=t.save(commit=False)
			c.uid_id=request.user.id
			c.save()
			messages.success(request,"Restaurant added Successfully")
			return redirect('/rlist')
		else:
			messages.warning(request,"Restaurant not added (File types not matched)")
			return redirect('/rlist')
 

	t=ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'alldata':alldata})


def update(request,m):
	k=Restaurant.objects.get(id=m)
	if request.method=="POST":
		e=ReForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Restaurant updated Successfully".format(k.rname))
			return redirect('/rlist')
	e=ReForm(instance=k)
	return render(request,'app/restupdate.html',{'x':e})


def delete(request,n):
	row=Restaurant.objects.get(id=n)
	if request.method=="POST":
		messages.info(request,"{} Restaurant deleted Successfully".format(row.rname))
		row.delete()
		return redirect('/rlist')
	return render(request,'app/restdelete.html',{'x':row})


def rstview(request,a):
	row=Restaurant.objects.get(id=a)
	items=Item.objects.filter(rsid=row.id)
	return render(request,'app/restview.html',{'z':row,'i':items})



def itemlist(request):
	#alldata=Item.objects.all()
	restaurants_of_user=list(Restaurant.objects.filter(uid_id=request.user.id))
	allitems=Item.objects.all()
	d,i={},0
	for item in allitems:
		for rest in restaurants_of_user:
			if rest.id==item.rsid_id:
				d[i]=item.itemname,item.itemtype,item.itemprice,item.availability,item.itemimg,item.id
				i+=1


	if request.method=="POST":
		t=ItemForm(request.POST,request.FILES)
		#print(t) for debug purpose
		if t.is_valid():  #Django validation
			n=t.save(commit=False)   #n.itemname is the item name and t.itemname is not the item name instead it is Html Form 
			#n.restaurant=request.user
			messages.success(request,"{} Item added Successfully".format(n.itemname))
			n.save()
			return redirect('/items')
		else:
			messages.warning(request,"Restaurant not added (File types not matched)")
			t.save()
			return redirect('/items')

	t=ItemForm()
	return render(request,'app/itemslist.html',{'r':t,'er':restaurants_of_user,'s':d.values()})

def itemview(request,a):
	row=Item.objects.get(id=a)
	print(row.itemname)
	return render(request,'app/itemview.html',{'x':row})



def updateitem(request,m):
	k=Item.objects.get(id=m)
	if request.method=="POST":
		e=ItemForm(request.POST,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} item updated Successfully".format(k.itemname))
			return redirect('/items')
	e=ItemForm(instance=k)
	return render(request,'app/itemupdate.html',{'q':e})


def deleteitem(request,n):
	row=Item.objects.get(id=n)
	if request.method=="POST":
		messages.info(request,"{} item deleted Successfully".format(row.itemname))
		row.delete()
		return redirect('/items')
	return render(request,'app/itemdelete.html',{'x':row})

def usrreg(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d=UsgForm()
	return render(request,'app/userregister.html',{'t':d})

#def itemview(request,id):
#	row=Item.objects.get(id=id)
#	row=ItemForm(instance=row)
#	if request.method=="POST":
#		#messages.info(request,"{} item deleted Successfully".format(row.itemname))
#		return redirect('/items')
#	return render(request,'app/itemview.html',{'i':row})

@login_required
def rolereq(request):
	p=Rolereq.objects.filter(ud_id=request.user.id).count()

	if request.method=="POST":
		k=Rltype(request.POST,request.FILES)
		if k.is_valid():
			y=k.save(commit=False)
			y.ud_id=request.user.id
			y.uname=request.user.username
			y.save()
			return redirect('/')

	k=Rltype()
	return render(request,'app/rolereq.html',{'d':k,'c':p})

def gveperm(request):
	u=User.objects.all()
	r=Rolereq.objects.all()
	d={}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id!=m.ud_id:
				continue
			else:
				d[n.id]=m.uname,m.rltype,n.role,m.id
	#print(d.values())
	return render(request,'app/gvper.html',{'h':d.values()})

def gvupdate(request,t):
	y=Rolereq.objects.get(id=t)
	d=User.objects.get(id=t)
	if request.method=="POST":
		n=Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked=1
			y.save()
			return redirect('/gvper')
	n=Rlupd(instance=d)
	#userrow=User.objects.get(id=row.ud_id)
	#if request.method=="POST":
	#	#row.uname=request.POST['uname']
	#	row.rltype=request.POST['rltype']
	#	userrow.role=request.POST['role']
	#	print(userrow.role)
	#	row.save()
	#	print("YESS")
	#	userrow.save()
	#	print("ALSO")
	#	return gveperm(request)
	#return render(request,'app/gvupdate.html',{'row':row,'u':userrow})
	return render(request,'app/gvupdate.html',{"n":n})

@login_required
def pfle(request):
	userdata=User.objects.get(id=request.user.id)
	#k=Profile(instance=userdata)
	return render(request,'app/profile.html',{"u":userdata})


def profileUpdate(request,id):
	userdata=User.objects.get(id=id)
	if request.method=="POST":
		userdata.username=request.POST.get('username')
		userdata.email=request.POST.get('email')
		userdata.mobilenumber=request.POST.get('mobile')
		userdata.age=request.POST.get('age')
		userdata.first_name=request.POST.get('fname')
		userdata.last_name=request.POST.get('lname')

		userdata.save()
		
		#d=Profile(request.POST,request.FILES,instance=userdata)
		#print(d)
		#userdata.username=request.POST['username']
		#userdata.first_name=request.POST['first_name']
	#k=Profile(instance=userdata)
		return pfle(request,id=id)
	return render(request,'app/profileupdate.html',{"us":userdata})

@login_required
def feedback(request):
	if request.method=="POST":
		sd=request.POST['snmail'].split(',')
		sm=request.POST['sub']
		mg=request.POST['msg']
		rt=settings.EMAIL_HOST_USER
		#sen_mail(sub,msg,sender,receivers)
		dt=send_mail(sm,mg,rt,sd)
		if dt==1:
			return redirect('/')
	return render(request,'app/feedback.html')

def pfleupd(request):
	t=User.objects.get(id=request.user.id)
	if request.method=="POST":
		pfle=Pfupd(request.POST,request.FILES,instance=t)
		if pfle.is_valid():
			pfle.save()
			return redirect('/pfle')
	pfle=Pfupd(instance=t) 
	return render(request,'app/pfleupdate.html',{'u':pfle})


def changepwd(request):
	if request.method=="POST":
		k=Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k=Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})