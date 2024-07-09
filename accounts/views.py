from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from reports.models import Report
from .models import *
from .forms import *
from django.contrib.auth import get_user_model


# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        # Ensure the username is case-insensitive
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username__iexact=username)
            # Authenticate with the original username case
            user = authenticate(request, username=user.username, password=password)
        except UserModel.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            if user.role == 'accountant':
                return redirect('a_dashboard') 
            elif user.role == 'admin':
                return redirect('dashboard') 
            elif user.role == 'manager':
                return redirect('manager_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')


########################################## profile page views
@login_required(login_url='login')
def profilePage(request):
    # user profile
    profile = get_object_or_404(Profile, user=request.user)

    # user profile form INSTANCE
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        # user profile form
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,  'Profile updated Successful✅')
            if request.user.role == 'admin':
                return redirect('dashboard')
            elif request.user.role == 'accountant':
                return redirect('reports')

    
        elif 'delete_account' in request.POST:
                profile.delete()
                messages.success(request, 'Account delete Successful')
                return redirect('login')
        
    # Fetch reports with the status 'correction' for the logged-in user[ notification ]
    correction_reports = Report.objects.filter(status='correction', account_owner=profile)

    # Fetch all reports with the status 'pending'[ notification ]
    pending_reports = Report.objects.filter(status='pending')

    context = {'form': form, 'profile': profile, 
               'correction_reports': correction_reports, 'pending_reports': pending_reports}
    return render(request, 'profile.html', context)


################################ logout views
def logoutPage(request):
    logout(request)
    return redirect('login')












