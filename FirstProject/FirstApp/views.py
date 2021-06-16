from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hi Welcome")

def htmltag(request):
	return HttpResponse("<h1>This is a heading</h1>")

def usernameprint(request,uname):
	return HttpResponse("<h1>Hi Welcome <span style='color:green'>{}</span></h1>".format(uname))

def favnum(request,n):
	return HttpResponse("<h1>Your Favourite number is:<span style='color:red'>{}</span></h2>".format(n))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center; background-color:cyan; padding:23px;font-size:25px'>Name:<span style='color:orange'>{}</span> and Age:<span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,eage,ename):
	return HttpResponse("<script>alert('Hi, Welcome {}')</script> Hi, Welcome {} and your age is:{} and your id is:{}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'ht1/first.html')

def ytname(request,name):
	return render(request,'ht1/ytname.html',{'n':name})

def empname(request,id,ename):
	d={'i':id,'n':ename}
	return render(request,'ht1/e.html',d)

def ownfun(request,nums):
	d={'numslist':nums}
	return render(request,'ht1/own.html',d)

def studentsdetails(request):
	return render(request,'ht1/std.html')

def alertfun(request):
	return render(request,'ht1/internaljs.html')

def myform(request):
	if request.method=="POST":
		#uname=request.POST['name']
		#print(uname)
		#print(request.POST)  this prints data in cmd 
		name=request.POST['name']
		regdno=request.POST['regdno']
		#email=request.POST['email'] or we can write using get() method POST is just a dictionary
		email=request.POST.get('email')
		#print(name,regdno,email)
		data={'name':name,'regdno':regdno,'email':email}
		return render(request,'ht1/formdetails.html',data)
	return render(request,'ht1/myform.html')

def myform2(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		phoneno=request.POST['phoneno']
		gender=request.POST['gender']
		address=request.POST['address']
		languages = request.POST.getlist('checks[]')
		sport=request.POST['sport']

		data={'fname':fname,'lname':lname,'email':email,'phoneno':phoneno,'gender':gender,'address':address,'languages':languages,'sport':sport}
		return render(request,'ht1/form2details.html',data)
	return render(request,'ht1/myform2.html')

def login(request):
	if request.method=='POST':
		if(request.POST['uname']=='siva' and request.POST['psw']=='siva'):
			uname=request.POST['uname']
			data={'uname':uname}
			return render(request,'ht1/success.html',data)
		else:
			return render(request,'ht1/error.html')
	return render(request,'ht1/login.html')
def bootstrapfun(request):
	return render(request,'ht1/usingbootstrap.html')