# Project Title: Employee Management System

## Project Description
The Employee Management System is a web application designed to manage employee records efficiently. It allows users to create, read, update, and delete employee information. The system supports features such as employee role assignment, department categorization, and automatic date recording for when employees are added.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete employees.
- **Filtering and Pagination**: Filter employees by department/role and paginate results.
- **Authentication**: JWT token-based authentication for secure access.

## Technologies Used
- **Backend Framework**: Django
- **REST Framework**: Django REST Framework
- **Testing**: Postman, Django's built-in testing framework
- **Environment Management**: Python virtual environment

## Installation Instructions

### Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository:
```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory
Change to the project directory:
```bash
cd <your-project-directory>
```

### Step 3: Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 4: Install Dependencies
Install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Running the Project

### Step 1: Apply Migrations
Run the following command to apply database migrations:
```bash
python manage.py migrate
```

### Step 2: Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### Step 3: Access the Application
Navigate to `http://127.0.0.1:8000/` in your web browser.

### Headers
In the Authorization tab, add:

        Auth Type: Bearer Token
        
        Token:your_access_token

In the Headers tab, add: 

        Key:Content-Type
        
        Value:application/json
        
Click Send to execute the request.
## Authentication
The API uses JWT (JSON Web Token) token-based authentication.

### Authorization
To access the protected API endpoints, you need to obtain a JWT token for authentication. This section will guide you through the process of getting the token and using it in your requests.

### Step 1: Creating a Superuser
Before obtaining the token, ensure you have a superuser account, which has permission to access the API.

**Steps to Create a Superuser:**
1. Open your terminal and navigate to your Django project directory.
2. Run the following command to create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
3. Follow the prompts to enter a username, email address, and password.

### Step 2: Get Token
To obtain your JWT token, send a `POST` request to the token endpoint.

- **URL**: `http://localhost:8000/api/token/`
- **Payload**:
```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```
- **Response**:
Upon successful authentication, you will receive a response containing the access and refresh tokens:
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

## API Documentation

### Base URL
All API requests will be made to the following base URL:
```
http://127.0.0.1:8000/api/
```

### Endpoints

#### 1. Create Employee
- **URL**: `/employees/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "name": "Emily Clark",
    "email": "emily.clark@example.com",
    "department": "Finance",
    "role": "Analyst"
}
```
- **Responses**:
  - **201 Created**: Employee created successfully.
  - **400 Bad Request**: Invalid data provided (e.g., email already exists).

#### 2. List Employees
- **URL**: `/employees/`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns a list of employees.
  - **404 Not Found**: No employees found.

#### 3. Retrieve Employee Details
- **URL**: `/employees/{id}/`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns details of the employee with the specified ID.
  - **404 Not Found**: Employee with the specified ID does not exist.

#### 4. Update Employee
- **URL**: `/employees/{id}/`
- **Method**: `PUT`
- **Request Body**:
```json
{
    "name": "Emily Clark",
    "email": "emily.clark@newdomain.com",
    "department": "Finance",
    "role": "Senior Analyst"
}
```
- **Responses**:
  - **200 OK**: Employee updated successfully.
  - **404 Not Found**: Employee with the specified ID does not exist.
  - **400 Bad Request**: Invalid data provided.

#### 5. Delete Employee
- **URL**: `/employees/{id}/`
- **Method**: `DELETE`
- **Responses**:
  - **204 No Content**: Employee deleted successfully.
  - **404 Not Found**: Employee with the specified ID does not exist.

## Testing the API
You can test the API using Postman or any other API testing tool. To create a new employee, use the `POST` method with the `/employees/` endpoint, providing the necessary JSON data in the body and including the required headers.

### Unit Tests
You can run the unit tests defined in your Django application using:
```bash
python manage.py test employees.test_views.EmployeeTests
```
Make sure to write tests for each endpoint, covering normal cases and edge cases, such as attempting to create an employee with an existing email.
