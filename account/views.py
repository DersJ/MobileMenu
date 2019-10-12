  
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from django.contrib.auth import get_user_model


from account.forms import SignUpForm, UpdateProfileForm


def loginview(request):
	return redirect('profile')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/account/profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/account/profile')
    else:
        initial = {
            'email': request.user.email,
            'phone': request.user.phone,
            'meals': request.user.meals,
            }
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form, 'user': request.user})

# class ProfileView(generic.DetailView):
#     template_name = 'registration/profile.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         now = timezone.now()

#         return context


#     def get_object(self):
#         return self.request.user