# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cusers
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/career/signin')
def home(request,param1='defaultvalue'):
	print(param1)
	x = {}
	x['flag'] = True
	#studentObjs = Student.objects.filter(full_name='student2')
	CusersObjs = Cusers.objects.all().order_by('uid')
	x['cusers']  = CusersObjs
	return render(request,'home.html',x)

@login_required(login_url='/career/signin')
def saveData(request):
	if request.method == "POST" :
		q1 = request.POST['q1']
		q2 = request.POST['q2']
		q3 = request.POST['q3']
		q4 = request.POST['q4']
		q5 = request.POST['q5']
		q6 = request.POST['q6']
		q7 = request.POST['q7']
		q8 = request.POST['q8']
		q9 = request.POST['q9']
		q10 = request.POST['q10']
		q11 = request.POST['q11']
		q12 = request.POST['q12']
		q13 = request.POST['q13']
		q14 = request.POST['q14']
		q15 = request.POST['q15']
				

		obj = Cusers()
		obj.q1 = q1
		obj.q2 = q2
		obj.q3 = q3
		obj.q4 = q4
		obj.q5 = q5
		obj.q6 = q6
		obj.q7 = q7
		obj.q8 = q8
		obj.q9 = q9
		obj.q10 = q10
		obj.q11 = q11
		obj.q12 = q12
		obj.q13 = q13
		obj.q14 = q14
		obj.q15 = q15
		obj.save()

	return redirect('/career/home')

def signin(request):
	response = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is None :
			return render(request, 'login.html', response)
		else :
			login(request,user)
			return redirect('/career/home')
	return render(request, 'login.html', response)