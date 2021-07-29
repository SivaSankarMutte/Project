#from django.forms import ModelForm
from RestApp.models import Restaurant,User,Rolereq
from RestApp.models import Item
#from django.contrib.auth.models import User  #Exixting User model
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms

class ReForm(forms.ModelForm): #Restaurant Form
	class Meta:
		model = Restaurant
		fields=['rname','nitems','timings','rsimg','address']
		widgets={
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter number of items available in Restaurant",
			}),
		"timings":forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter the Restaurant Timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter address",
			"rows":3,
			}),		
		}



class ItemForm(forms.ModelForm):
	class Meta:
		model=Item
		#fields="__all__"
		fields=['rsid','itemname','itemtype','itemprice','availability','itemimg']
		widgets={
		"rsid":forms.Select(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"itemname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter item name"			
			}),
		"itemtype":forms.Select(attrs={
			"class":"form-control my-2",

			}),
		"itemprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter price",
			}),
		"itemavailability":forms.Select(attrs={
			"class":"form-control my-2",
			})
		}
	#def __init__(self,user,*args,**kwargs):
	#	super(ItemForm,self).__init__(*args,**kwargs)
	#	self.fields['rsid'].queryset=Restaurant.objects.filter(userid_id=user.id)
		


class UsgForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm Password",
		}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter User Name",
			}),

		}

class Rltype(forms.ModelForm):
	class Meta:
		model=Rolereq
		fields=['uname','rltype','pfe']
		widgets={
		"uname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,

			}),
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','role']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}


class Pfupd(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','age','mobilenumber','uimg']
		widgets={
		"uimg":forms.FileInput(attrs={
			"class":"form-control my-2",
			"null":True,
			"blank":True,
			"required":False,
			}),
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter User Name",
			"blank":True,
			"required":False,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter First Name",
			"null":True,
			"blank":True,
			"required":False,
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Last Name",
			"null":True,
			"blank":True,
			"required":False,
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Email",
			"null":True,
			"blank":True,
			"required":False,
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Age",
			"null":True,
			"blank":True,
			"required":False,
			}),
		"mobilenumber":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number",
			"null":True,
			"blank":True,
			"required":False,
			}),
		# "role":forms.NumberInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"required":False,
		# 	}),
		# "is_staff":forms.NumberInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"required":False,
		# 	}),
		# "is_active":forms.NumberInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"required":False,
		# 	}),
		# "is_superuser":forms.NumberInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"required":False,
		# 	}),
		# "date_joined":forms.DateTimeInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"required":False,
		# 	}),
		# "last_login":forms.DateTimeInput(attrs={
		# 	"class":"form-control my-2",
		# 	"readonly":True,
		# 	"null":True,
		# 	"blank":True,
		# 	"required":False,
		# 	}),

		}

class Chgepwd(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Old Password",
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter new Password",
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm new Password",
		}))

	class Meta:
		model=User
		fields=['old_password','new_password1','new_password2']
		