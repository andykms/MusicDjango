from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm

@login_required 
def dashboard(request): 
  return render( request, './striming/dashboard.html',
  {'section': 'dashboard'}) #Последнее это секция,  о ней ниже

def register(request): 
  if request.method == 'POST': 
    user_form = UserRegistrationForm(request.POST) 
    if user_form.is_valid(): 
      new_user = user_form.save(commit=False) 
      new_user.set_password(user_form.cleaned_data['password'])
      return render( 
        request, 
        'striming/register_done.html', 
        {'new_user': new_user} 
      ) 
  else: 
    user_form = UserRegistrationForm() 
  return render( request, 'striming/register.html', {'user_form': user_form} )
