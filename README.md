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
- Go to the Body tab.
- Select the raw option.
- In the dropdown next to raw, select JSON.
- Write your payload in the text area. For example
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
The test_views.py file is designed to contain unit tests for the views associated with the employee management API. It serves the purpose of validating that the various endpoints of the API function as expected, ensuring that all CRUD (Create, Read, Update, Delete) operations behave correctly under different conditions. This testing is essential for maintaining the integrity of the application as changes are made to the codebase.

Purpose of test_views.py
Validate API Functionality: The tests ensure that each API endpoint behaves as intended, returning the correct HTTP status codes and responses for different scenarios.
Catch Bugs Early: By writing tests for both normal and edge cases, we can identify and fix potential issues before they reach production.
Facilitate Future Development: Well-defined tests make it easier for developers to understand the expected behavior of the API and to ensure that new changes do not break existing functionality.
Key Components of the Testing Process
Setup:

Import necessary modules from Django and the Django REST framework.
Define the test class that inherits from APITestCase, which provides utility methods for testing API views.
Writing Test Cases:

Each test case is defined as a method within the test class. The naming convention typically starts with test_ followed by a description of the functionality being tested.
Use the self.client object to simulate requests to the API.
Common Test Scenarios:

Creating an Employee: Test that valid employee data can be submitted and results in a successful creation (HTTP 201) with the correct details stored.
Handling Duplicate Emails: Test that attempting to create an employee with an existing email address results in a proper error response (HTTP 400).
Retrieving Employee Details: Validate that a specific employee's information can be fetched using their ID, ensuring the response is correct and complete.
Updating Employee Information: Verify that an employee's details can be modified successfully, confirming that changes are reflected in the database.
Deleting an Employee: Test that an employee can be removed from the system and that the appropriate response (HTTP 204) is returned.
Not Found Cases: For both retrieval and deletion, ensure that requesting a non-existent employee results in a 404 Not Found response.
Running the Tests:

Use the Django management command python manage.py test employees.test_views.EmployeeTests to execute the tests.
This command will run all the test methods within the EmployeeTests class and report any failures or errors encountered during the testing process.
