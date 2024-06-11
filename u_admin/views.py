from django.http import HttpResponse
from accounts.models import Profile
from .forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reports.forms import ReportCreationForm
from django.http import HttpResponse
from openpyxl import Workbook
from reports.models import Report
from openpyxl.utils import get_column_letter
from io import BytesIO
from reports.filters import ReportFilter
from .forms import ProfileUpdateForm, UserUpdateForm


# admin dashboard view
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')
    
    user = request.user.profile
    form = ReportCreationForm()

    # Apply the filter
    reports = Report.objects.select_related('account_owner').all()
    report_filter = ReportFilter(request.GET, queryset=reports)
    reports = report_filter.qs

    # get total pending reports
    pending_reports_count = Report.objects.filter(status='pending').count()

    if request.method == "POST":
        form = ReportCreationForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.account_owner = user
            if request.user.role == "admin":
                report.status = 'approve'
            report.save()
            return redirect('dashboard')
        
    context = {'form': form, 'reports': reports, 
               'filter': report_filter, 'reports_count': pending_reports_count}

    if request.htmx:
        return render(request, 'reports/partials/reports-list.html', context)
    
    return render(request, 'u_admin/admin_dashboard.html', context)


# user_management view
@login_required
def user_management(request):
    if request.user.role != 'admin':
        return redirect('login')
    
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


# download_report view
def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    # Create a workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Report"

    # Define the headers
    headers = ["Username", "Date", "Description", "Main Category", "Sub Category", "Payment"]
    worksheet.append(headers)

    # Add the report data
    formatted_date = report.created_time_stamp.strftime('%d %B, %Y') if report.created_time_stamp else None
    report_data = [
        report.account_owner.username,
        formatted_date,
        report.description,
        report.main_category,
        report.sub_category,
        str(report.payment)
    ]
    worksheet.append(report_data)

    # Adjust column widths
    column_widths = []
    for row in worksheet.iter_rows(values_only=True):
        for i, cell in enumerate(row):
            if len(column_widths) > i:
                if len(str(cell)) > column_widths[i]:
                    column_widths[i] = len(str(cell))
            else:
                column_widths += [len(str(cell))]

    for i, column_width in enumerate(column_widths, 1):
        worksheet.column_dimensions[get_column_letter(i)].width = column_width + 2

    # Save the workbook to a BytesIO stream
    output = BytesIO()
    workbook.save(output)
    output.seek(0)

    # Set the response as an Excel file
    response = HttpResponse(
        content=output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=report_{report_id}.xlsx'

    return response


@login_required
def update_user(request, pk):
    if request.user.role != 'admin':
        return redirect('login')

    profile = get_object_or_404(Profile, id=pk)
    user = profile.user

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'u_admin/edit-user.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    })