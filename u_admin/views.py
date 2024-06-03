from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# dashboard view
@login_required
def dashboard(request):
    return render(request, 'u_admin/admin_dashboard.html')
