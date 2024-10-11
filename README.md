
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


## Setup Instructions for Resume Uploader with Docker and Elasticsearch
# Prerequisites:
Before getting started, ensure the following software is installed on your system:

Docker Desktop (for Windows/macOS/Linux)
Git (optional, for cloning the repository)
# Step 1: Clone the Repository
If you haven't already, clone the project repository to your local machine:
git clone https://github.com/your-username/resume-uploader.git
cd resume-uploader
# Step 2: Set Up Docker and Elasticsearch
The project uses Docker to handle dependencies like Elasticsearch. This simplifies the setup by bundling everything into a containerized environment.

Ensure Docker Desktop is Running:
Make sure Docker is installed and running on your system.

Run the Docker Setup:
Navigate to the project directory and run the following command to start Elasticsearch and other services:
docker-compose up
This will:

Download and start Elasticsearch in a Docker container.
Start the Django app and any other services you’ve defined in docker-compose.yml.
Access the Application: Once the containers are up and running:

Your Django application will be available at: http://localhost:8000
Elasticsearch will be available at: http://localhost:9200
# Elasticsearch Notes:
Elasticsearch is required for the resume search functionality in the application. By using Docker, Elasticsearch will automatically start as a service, so there's no need to download or manually configure it.

Important: If Docker is not running, the resume search feature will not work since Elasticsearch will be unavailable.
# Step 3: Testing Elasticsearch
To confirm that Elasticsearch is running properly, you can access the following URL in your browser or use curl:
http://localhost:9200
This should return a JSON response indicating the Elasticsearch status.

# Troubleshooting:
If Docker Desktop or WSL (for Windows) crashes, try restarting Docker or run the following command to restart WSL:
wsl --shutdown

