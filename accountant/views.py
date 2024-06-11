from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reports.forms import ReportCreationForm
from django.http import HttpResponse
from openpyxl import Workbook
from reports.models import Report
from django.contrib import messages
from openpyxl.utils import get_column_letter
from io import BytesIO
from reports.filters import ReportFilter
import pandas as pd
from reports.forms import UploadFileForm
from accounts.models import Profile
from openpyxl import load_workbook


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if not file.name.endswith('.xlsx'):
                messages.error(request, 'The uploaded file is not an Excel file.')
                return redirect('upload_file')
            try:
                # Verify the file is an Excel file by attempting to load it
                load_workbook(file)
                data = pd.read_excel(file, engine='openpyxl')
                for index, row in data.iterrows():
                    try:
                        account_owner = Profile.objects.get(username=row['username'])
                    except Profile.DoesNotExist:
                        messages.error(request, f"Profile with username {row['username']} does not exist.")
                        continue
                    Report.objects.create(
                        account_owner=account_owner,
                        description=row['description'],
                        main_category=row['main category'],
                        sub_category=row['sub category'],
                        status=row['status'],
                        payment=row['payment'],
                    )
                messages.success(request, 'File uploaded and reports created successfully.')
                return redirect('upload_file')
            except Exception as e:
                messages.error(request, f'Error processing file: {e}')
    else:
        form = UploadFileForm()
    return render(request, 'accountant/upload-reports.html', {'form': form})


# create_report view
@login_required(login_url='login')
def create_report(request):
    if request.user.role != 'accountant':
        return redirect('login')
    user = request.user.profile
    form = ReportCreationForm()

    # Apply the filter
    reports = Report.objects.select_related('account_owner').all()
    report_filter = ReportFilter(request.GET, queryset=reports)
    reports = report_filter.qs

    if request.method == "POST":
        form = ReportCreationForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.account_owner = user
            report.save()
            return redirect('reports')
        
    context = {'form': form, 'reports': reports, 'filter': report_filter}

    if request.htmx:
        return render(request, 'reports/partials/reports-list.html', context)

    return render(request, 'accountant/reports.html', context)


# download_report view
def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    # Create a workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Report"

    # Define the headers
    headers = ["username", "date", "description", "main category", "sub category", "payment"]
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
