from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect 
def index(request):
	return render(request,'index/index.html',)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')		