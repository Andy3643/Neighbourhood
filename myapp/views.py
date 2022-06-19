from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
#from django.contrib.auth.decorators import login_required


# Create your views here. 
  
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
def Index_view(request):
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




#@login_required
def profile(request):
    '''
    This method handles the user profile 
    '''
    title = 'Profile'
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"You Have Successfully Updated Your Profile!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title':title,
        'u_form':u_form,
        'p_form':p_form 
    }
    return render(request,'users/profile.html',context)


#@login_required
def create_story(request):
    '''
    will handle the creation of neihbourhood storys
    '''
    current_user = request.user
    current_user_neighborhood = request.user.profile.neighborhood
    title = "Post a story"
    if current_user_neighborhood:
        if request.method == "POST":
            form = NeighborhoodStoryForm(request.POST)
            if form.is_valid():
                story = form.save(commit=False)
                story.user = current_user
                story.neighborhood = current_user_neighborhood
                story.save()
                return redirect(Index_view)
        else:
            form = NeighborhoodStoryForm()
            return render(request,"main/post_story.html",{"form":form})
    else:
        messages.warning(request,"Please Join a neighbourhood to post a story")
        return redirect(Index_view)



#@login_required
def person_info(request):
    '''
    will show users profile and their neighbours
    '''
    current_user = request.user
    profile = request.user.profile
    current_neighborhood_user = request.user.profile.neighborhood
    neighbours = Profile.objects.filter(neighborhood=current_neighborhood_user)
    context = {
        "neighbours":neighbours.exclude(user=current_user),
        "profile":profile,
        "current_user":current_user
    }

    return render(request,"users/my_profile.html",context)



#@login_required
def add_buisness(request):
    '''
    This view will handle user adding buisness to neighbourehood 
    '''
    current_user_neighborhood = request.user.profile.neighborhood
    if request.method == "POST":
        form = NeighborhoodBuisnessesForm(request.POST)
        if form.is_valid():
            buisness = form.save(commit=False)
            buisness.user = request.user
            buisness.neighborhood = current_user_neighborhood
            buisness.save()
            return redirect(Index_view)
    else:
        form = NeighborhoodBuisnessesForm()
        return render(request,"main/buisness_form.html",{"form":form})