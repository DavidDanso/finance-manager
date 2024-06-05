from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .forms import UserCreationForm


# dashboard view
@login_required
def dashboard(request):
    return render(request, 'u_admin/admin_dashboard.html')


# user_management view
@login_required
def user_management(request):
    if request.user.role != 'admin':
        return HttpResponse('<h1>You do not have admin access to view this page</h1>')
    users = Profile.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('users')
    else:
        form = UserCreationForm()
    context = {'users': users, 'form': form}
    return render(request, 'u_admin/user_management.html', context)