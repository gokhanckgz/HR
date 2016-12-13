from django.shortcuts import render
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.http import *

def login_page(request):
	form = AuthenticationForm
	if(request.method=='POST'):
		username = request.POST['username']
		password = request.POST['password']
		user = AuthenticationForm(data=request.POST)
		if(user.is_valid()):
			kullanici = authenticate(username=username,password=password)
			login(request,kullanici)
			if kullanici.user_type=='Supplier':
				return HttpResponseRedirect('/supplier/')
			elif kullanici.user_type=='Company':
				return HttpResponseRedirect('/company/')
			elif kullanici.user_type=='Employe':
				return HttpResponseRedirect('/employee/')
	return render(request,'login/index.html',locals())

