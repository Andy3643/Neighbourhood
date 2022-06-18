from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
#from django.contrib.auth.decorators import login_required


# Create your views here.
def Index_view(request):
      return render(request,"index.html")   
  
def register(request):
    '''
    Function to register new users to the database.
    '''
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"You have succesfully created an account. Proceed to Login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"users/sign-up.html",context)

#Home page
#@login_required
def index_view(request):
    '''
    Main home page view
    '''
    current_user = request.user
    current_neighborhood_user = request.user.profile.neighborhood
    if current_neighborhood_user == None:
        messages.info(request,"Please join a neibourhood to engage by updating your profile") 
    title = "home"
    user_status = Neighborhood.objects.filter(admin=current_user)
    neighborhood_stories = Stories.objects.filter(neighborhood=current_neighborhood_user)
    neighborhood_contacts = Neighborhood_contact.objects.filter(neighborhood=current_neighborhood_user)
    neighborhood_business = Business.objects.filter(neighborhood=current_neighborhood_user)
    neighborhood_announcements = Announcement.objects.filter(neighborhood=current_neighborhood_user)

    context = {
        "title":title,
        "neighborhood_stories":neighborhood_stories,
        "neighborhood_contacts":neighborhood_contacts,
        "neighborhood_business":neighborhood_business,
        "neighborhood_announcements":neighborhood_announcements,
        "admin":user_status
    }

    return render(request,"index.html",context)