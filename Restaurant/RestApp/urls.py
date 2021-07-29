from django.urls import path
from RestApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as v

urlpatterns=[
	path('',views.home,name="home"),
	path('about/',views.about,name="about"),
	path('contact/',views.contact,name="contact"),
	#path('login/',views.login,name="login"),
	path('rlist/',views.restlist,name="rlist"),
	path('update/<int:m>/',views.update,name="update"),
	path('delete/<int:n>/',views.delete,name="delete"),
	path('rstview/<int:a>/',views.rstview,name="rsvw"),
	path('items/',views.itemlist,name="items"),
	path('updateitem/<int:m>/',views.updateitem,name="updateitem"),
	path('deleteitem/<int:n>/',views.deleteitem,name="deleteitem"),
	path('itemview/<int:a>/',views.itemview,name='itemview'),
	path('rg/',views.usrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="app/login.html"),name="login"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
	path('roltype/',views.rolereq,name="rlrq"),
	path('gvper/',views.gveperm,name='gvpm'),
	path('gvup/<int:t>/',views.gvupdate,name="gvup"),
	path('pfle/',views.pfle,name="pf"),
	path('pfupd/',views.pfleupd,name="pfup"),
	path('profileupdate/<int:id>/',views.profileUpdate,name="profileupdate"),
	path('fdb/',views.feedback,name="fd"),
	path('chge/',views.changepwd,name="chpd"),
] 

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 