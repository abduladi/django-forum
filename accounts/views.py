from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from accounts.forms import SignUpForm

# Create your views here.


def signup(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			user = form.save()
			
			login(request, user)

			return redirect('home')

	else:

		form = SignUpForm()


	context = {'form': form}
	
	return render(request, 'signup.html', context)