# Expense Management System

This project is a Django-based Expense Management System application with role-based authentication and permissions for two user roles, 
Admin and Accountant, each having its own dashboard and permissions, allowing users to edit their profiles; it is built using Django, 
NeonDB for serverless Postgres, and Render for hosting, and consists of two main interfaces: the Accountant Dashboard and the Admin Dashboard.

## Table of Contents

- Features
- Technologies Used
- Setup and Installation
- Usage
- Project Interface

## Features

### Accountant Dashboard
- Input fields for Date, Description, Main Category, Sub Category, and Payments.
- Notifications from the admin for corrections or changes.
- Ability to upload data using an Excel file.
- Menu displaying records sent back for changes by the admin.
- Reset password

### Admin Dashboard
- Approve/reject requests for modifications or Excel file uploads.
- Generate and view reports.
- Modify records directly.
- Manage users (create/delete users, change permissions).
- Menu displaying records pending for approval from accountants.
- Detailed view of records with the ability to approve or send back for corrections.
- Notifications for corrections or changes.
- Modify records after approval based on specified date.

## Technologies Used
- Django: Web framework for developing the application.
- PostgreSQL: Database management system.
- NeonDB: For serverless Postgres Config.
- AWS S3: Static files for the application.
- Render: Continuous deployment and hosting platform.

## Setup and Installation

### Prerequisites
- AWS account setup for S3.
- Render account setup.
- NeonDB account setup.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DavidDanso/finance-manager.git
   cd finance-manager

2. Set Up Environment Variables
    Create a .env file in the root directory and add your environment variables:

   ```
    DEBUG=1
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    AWS_ACCESS_KEY_ID=your_aws_access_key_id
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
    ```
    
4. Create a virtual environment:

   ```bash
   python3 -m venv env


5. Activate the virtual environment:
   
   ### On macOS and Linux:

   ```bash
   source env/bin/activate


6. Install the required dependencies::

   ```bash
   pip install -r requirements.txt


7. Apply Migrations:

   ```bash
   python manage.py migrate \
   python manage.py makemigrations


8. Create a Superuser:

   ```bash
   python manage.py createsuperuser


9. Collect Static Files:

   ```bash
   python manage.py collectstatic
   

## Usage

- Accountant: Log in to the Accountant Dashboard to manage entries, upload data, and view notifications.
- Admin: Log in to the Admin Dashboard to approve/reject reports, manage users, generate reports, review records, approve or send back entries for corrections, and modify records.


## Project Interface

<table width="100%"> 
  <tr>
    <td width="50%">      
    &nbsp; 
    <br>
    <p align="center">
      Accountant Dashboard
    </p>
    <img src="https://github.com/DavidDanso/finance-manager/blob/main/static/images/ui/accountant.png" />
    </td>
    <td width="50%">      
    &nbsp; 
    <br>
    <p align="center">
      Admin Dashboard
    </p>
    <img src="https://github.com/DavidDanso/finance-manager/blob/main/static/images/ui/admin.png" />
    </td>
  </tr>

   <tr>
    <td width="50%">      
    &nbsp; 
    <br>
    <p align="center">
      Notification Modal
    </p>
    <img src="https://github.com/DavidDanso/finance-manager/blob/main/static/images/ui/notification.png" />
    </td>
    <td width="50%">      
    &nbsp; 
    <br>
    <p align="center">
      Excel Upload
    </p>
    <img src="https://github.com/DavidDanso/finance-manager/blob/main/static/images/ui/upload_excel.png" />
    </td>
  </tr>
</table>


## Author
David Danso - Initial work - [GitHub Profile](https://github.com/DavidDanso)

##### Email: davidkellybrownson@gmail.com

### Happy Coding!
