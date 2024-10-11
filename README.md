
# Resume Portal 

## Introduction

The Resume Uploader Project is a resume portal that allows authorized users to upload single or multiple resumes in DOC and PDF formats, provided they have the necessary permissions. 

This project features an advanced elastic search capability, enabling users to search resumes based on their content. Additionally, top-level users can create or register employees. Once an employee is registered, their credentials are automatically sent to their respective email addresses.

The system includes a master module for managing roles, companies, locations, and employees, as well as a main module for handling resume uploads. Resumes are categorized and uploaded based on the specified role, location, and company.

## Features

- **Elastic Search:** Powerful search functionality that retrieves resumes based on content.
- **Inbuilt Django Authentication:** Secure user authentication mechanism.
- **Custom User Model:** Utilizes Django’s `AbstractUser` to create a customized user model.
- **Multiple Resume Uploads:** Allows users to upload multiple resumes simultaneously and remove them as needed.
- **Organized Resume Storage:** Resumes are uploaded to specific folders based on their roles (e.g., resumes for Python developers are stored in the Python folder, while those for React developers are stored in the React folder).
- **Role-Based Authentication:** Access to modules is restricted based on user permissions, ensuring only authorized employees can access certain features.
- **SMTP Implementation:** Email notifications are sent seamlessly using SMTP for sending credentials to newly registered employees.
- **Validation:** Includes both client-side and server-side validation to ensure data integrity and improve user experience.
- **DataTable Feature:** Includes functionalities for searching, sorting, filtering, and pagination, allowing users to view 5, 10, 50, or 100 records per page.


For a detailed view of the application, please see the presentation:
https://github.com/raiyan201/resume-uploader_new/blob/master/Resume_presentation/resume%20Portal%20presentation.pdf
