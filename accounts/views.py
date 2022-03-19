from django.shortcuts import render, redirect

# Create your views here
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:otp")
    template_name = "accounts/signup.html"

# def signup(request):
# 	if request.method == "POST":
# 		form = UserCreateForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			# messages.success(request, "Registration successful." )
# 			return redirect("home")
# 		# messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = UserCreateForm()
# 	return render (request=request, template_name="accounts/signup.html", context={"form":form})

def otp(request):
	if request.method == "POST":
		code = request.POST.get("otp")
		if code == '123456':
			return redirect("accounts:login")
	
	return render(request, 'accounts/otp.html')
