from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import Post
from Calorie_Chart.models import Veg , Fruits, Carb, Protein, Fat, Others


# Create your views here.
def home(request):
	all_post = Post.objects.all()
	context = {'all_post_list':all_post}
	return render(request, 'index.html', context)

def user_signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			# create user
			User.objects.create_user(username=username, email=email, password=password)
			messages.success(request, 'User Registration Successfully')
			return redirect('/login')
	form = SignUpForm()
	return render(request, 'signup.html', {'signup_form': form})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			messages.error(request, 'this is fail')
			return HttpResponse("Username or password incorrect")
	return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def single_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	print(post)
	return render(request, 'post_detail.html', {'post':post})

def bmi(request):
	return render(request, 'bmi.html')

def bmr(request):
	return render(request, 'bmr.html')

def tdee(request):
	return render(request, 'tdee.html')

def calorie_chart(request):
	all_veg = Veg.objects.all()
	all_fruits = Fruits.objects.all()
	all_carb = Carb.objects.all()
	all_protein = Protein.objects.all()
	all_fat = Fat.objects.all()
	all_others = Others.objects.all()

	context = {
					'all_veg_list':all_veg,
					'all_fruit_list':all_fruits,
					'all_carb_list':all_carb,
					'all_protein_list':all_protein,
					'all_fat_list':all_fat,
					'all_others_list':all_others
					}
	return render(request, 'calorie.html', context)

def diet_chart(request):
	return render(request, 'diet_chart.html')
