<<<<<<< HEAD
                            # **Project Title: Employee Management System**

Project Description
The Employee Management System is a web application designed to manage employee records efficiently. It allows users to create, read, update, and delete employee information. The system supports features such as employee role assignment, department categorization, and automatic date recording for when employees are added.

Technologies Used
Backend Framework: Django
REST Framework: Django REST Framework
Testing: Postman, Django's built-in testing framework
Environment Management: Python virtual environment

## Objective
Build a basic REST API to manage employees in a company, focusing on CRUD operations, RESTful principles, and authentication.

**Installation Instructions**
Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository:
    git clone <your-repository-url>
Step 2: Navigate to the Project Directory
Change to the project directory:
    cd <your-project-directory>
Step 3: Set Up a Virtual Environment
Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Step 4: Install Dependencies
Install the required dependencies listed in requirements.txt:
    pip install -r requirements.txt
**Running the Project**
Step 1: Apply Migrations
Run the following command to apply database migrations:
    python manage.py migrate
Step 2: Run the Development Server
Start the Django development server:
    python manage.py runserver

Access the application by navigating to http://127.0.0.1:8000/ in your web browser.
### Headers
Make sure to include the following headers in your request:
        Key:Content-Type
        Value:application/json
        Authorization: Bearer your_access_token
**Authentication**
The API uses JWT token-based authentication.

Authorization

To access the protected API endpoints, you need to obtain a JWT (JSON Web Token) for authentication. This section will guide you through the process of getting the token and using it in your requests.

1. Creating a Superuser

Before obtaining the token, ensure you have a superuser account, which has permission to access the API.

Steps to Create a Superuser:
1. Open your terminal and navigate to your Django project directory.
2. Run the following command to create a superuser:
   python manage.py createsuperuser
3. Follow the prompts to enter a username, email address, and password.

2. Get Token:

URL: POST http://localhost:8000/api/token/
Payload:
json
=======
# Project Title: Employee Management System

## Project Description
The Employee Management System is a web application designed to manage employee records efficiently. It allows users to create, read, update, and delete employee information. The system supports features such as employee role assignment, department categorization, and automatic date recording for when employees are added.

## Features
-**CRUD Operations**: Create, Read, Update, and Delete employees.

-**Filtering and Pagination**: Filter employees by department/role and paginate results.

-**Authentication**: JWT token-based authentication for secure access.

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
Make sure to include the following  in your requests:
In the Authorization tab, add:
        Auth Type: Bearer Token
        Token:your_access_token

Make sure to include the following Headers in your request:
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
>>>>>>> 2728bc94539dd1ac8438f2564751a55c7774673e
{
  "username": "yourusername",
  "password": "yourpassword"
}
<<<<<<< HEAD
Response:
Upon successful authentication, you will receive a response containing the access and refresh tokens
=======
```
- **Response**:
Upon successful authentication, you will receive a response containing the access and refresh tokens:
```json
>>>>>>> 2728bc94539dd1ac8438f2564751a55c7774673e
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
<<<<<<< HEAD
**Create an Employee**

This section outlines how to create a new employee record in the system using the API.

### 1. Endpoint

- URL: POST http://localhost:8000/api/employees/

### 2. Request Payload
To create an employee, you need to send a JSON payload in the request body with the required fields. The `date_joined` field is auto-generated and should not be included in the request.
Payload Example:
{
  "name": "Emily Clark",
  "email": "emily.clark@example.com",
  "department": "Finance",
  "role": "Analyst"
}

### 3. Headers
Make sure to include the following headers in your request:
        Key:Content-Type
        Value:application/json
        Authorization: Bearer your_access_token

### 4. Example Request in Postman
        In the Body tab, select raw and enter the JSON payload as shown above.
        Click Send to execute the request.

### 5. Error Handling
If there are validation errors, you will receive a response with a status code of 400 Bad Request along with a message describing the issue. For example:

Example Error Response:

{
  "email": ["This field must be unique."]
}

**List all Employees**
This section outlines how to retrieve a list of all employee records from the system using the API.

## 1. Endpoint
URL: GET http://localhost:8000/api/employees/

## 2. Headers
In the Headers tab, add:
        Authorization: Bearer 
        Value:your_access_token
        Click Send to execute the request.

## 4. Response
Upon successful retrieval of employee records, you will receive a response with a status code of 200 OK and a JSON array containing all employees.

Example Response:

[
  {
    "id": 1,
    "name": "Emily Clark",
    "email": "emily.clark@example.com",
    "department": "Finance",
    "role": "Analyst",
    "date_joined": "2024-11-03"
  },
  {
    "id": 2,
    "name": "David Grey",
    "email": "david.grey@example.com",
    "department": "Engineering",
    "role": "Developer",
    "date_joined": "2024-11-02"
  }
]

**Retrieve a Single Employee**
This section outlines how to retrieve a specific employee record from the system using their unique identifier (ID).

### 1. Endpoint
URL: GET http://localhost:8000/api/employees/{id}/
Replace {id} with the actual ID of the employee you want to retrieve.

## 2. Headers
In the Headers tab, add:
        Authorization: Bearer 
        Value:your_access_token
        Click Send to execute the request.

### 3. Response
Upon successful retrieval of the employee record, you will receive a response with a status code of 200 OK and a JSON object containing the employee's details.

Example Response:

{
  "id": 1,
  "name": "Emily Clark",
  "email": "emily.clark@example.com",
  "department": "Finance",
  "role": "Analyst",
  "date_joined": "2024-11-03"
}

### 4. Error Handling
If the specified employee ID does not exist in the database, you will receive a response with a status code of 404 Not Found.

Example Error Response:

{
  "detail": "Not found."
}

If the token is invalid or missing, you will get a response with a status code of 401 Unauthorized.

Example Error Response:

{
  "detail": "Authentication credentials were not provided."
}
By following these steps, you can retrieve a single employee's record from the system through the API.

**Update an Employee**

### 1. Endpoint
URL: PUT http://localhost:8000/api/employees/{id}/
Replace {id} with the actual ID of the employee you want to update.
### 2.Request Payload
{
  "name": "Emily Clark",
  "email": "emily.clark_updated@example.com",
  "department": "Sales",
  "role": "Senior Analyst"
}

### 3. Headers
Make sure to include the following headers in your request:
        Content-Type: application/json
        Authorization: Bearer your_access_token
        Click Send to execute the request.

### 4. Response
Upon successfully updating the employee record, you will receive a response with a status code of 200 OK and a JSON object containing the updated details of the employee.

{
  "id": 1,
  "name": "Emily Clark",
  "email": "emily.clark_updated@example.com",
  "department": "Sales",
  "role": "Senior Analyst",
  "date_joined": "2024-11-03"
}
### 5. Error Handling
If the specified employee ID does not exist, you will receive a response with a status code of 404 Not Found.

Example Error Response:

{
  "detail": "Not found."
}
If the token is invalid or missing, you will receive a response with a status code of 401 Unauthorized.

Example Error Response:

{
  "detail": "Authentication credentials were not provided."
}
If there is a validation error (e.g., duplicate email), you will get a 400 Bad Request response with details about the issue.

Example Error Response:

{
  "email": ["This field must be unique."]
}

**Delete an Employee**

This section outlines how to delete an employee record in the system using the employee's unique identifier (ID).

### 1. Endpoint

URL: DELETE http://localhost:8000/api/employees/{id}/

Replace `{id}` with the actual ID of the employee you want to delete.

### 2. Headers
Make sure to include the following headers in your request:
        Content-Type: application/json
        Authorization: Bearer your_access_token
        Click Send to execute the request.

### 3. Response

Upon successfully deleting the employee record, you will receive a response with a status code of 204 No Content. This indicates that the deletion was successful, and there is no content in the response body.

### 4. Error Handling

If the specified employee ID does not exist, you will receive a response with a status code of 404 Not Found.

Example Error Response:
{
  "detail": "Not found."
}

If the token is invalid or missing, you will receive a response with a status code of 401 Unauthorized.

Example Error Response:
{
  "detail": "Authentication credentials were not provided."
}

**Filtering Employees by Department and Role**

This section describes how to filter employee records based on department and role.

### 1. Endpoint

- URL: `GET http://localhost:8000/api/employees/`
- Filtering Parameters: You can filter results by appending query parameters to the URL.

   - `department`: Filters employees by department (e.g., `HR`, `Engineering`, `Sales`).
   - `role`: Filters employees by role (e.g., `Manager`, `Developer`, `Analyst`).

### 2. Example Requests

- Filter by Department:  
  `GET http://localhost:8000/api/employees/?department=HR`

- Filter by Role:  
  `GET http://localhost:8000/api/employees/?role=Developer`

- Filter by Both Department and Role:  
  `GET http://localhost:8000/api/employees/?department=HR&role=Manager`

### 3. Headers
Make sure to include the following headers in your request:

        Authorization: `Bearer your_access_token`
        Click Send to execute the request


### 4. Example Response

Upon success, you’ll receive a JSON response containing employee records that match the specified filters.

Example Response:

[
  {
    "id": 2,
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "department": "Finance",
    "role": "Analyst",
    "date_joined": "2024-10-10"
  },
  {
    "id": 3,
    "name": "Bob Williams",
    "email": "bob.williams@example.com",
    "department": "Finance",
    "role": "Analyst",
    "date_joined": "2024-10-12"
  }
]

### 5. Error Handling

If no employees match the filter criteria, you will receive an empty array `[]` with a 200 OK status.

If the token is invalid or missing, you will receive a 401 Unauthorized status.

Example Error Response:
{
  "detail": "Authentication credentials were not provided."
}

**Pagination for Employee Records**

This section explains how to retrieve employee records with pagination, limiting results to 10 employees per page.

### 1. Endpoint

- URL: `GET http://localhost:8000/api/employees/`
- Pagination Parameter:  
  Use the `page` query parameter to navigate through paginated results. For example, `?page=2` will retrieve the second set of 10 employees.

### 2. Example Requests

- First Page (default):  
  `GET http://localhost:8000/api/employees/?page=1`

- Second Page:  
  `GET http://localhost:8000/api/employees/?page=2`

### 3. Headers

Make sure to include the following headers in your request:

    - Authorization: `Bearer your_access_token`
      - Click Send to execute the request.

### 4. Example Response

The response will contain a JSON array with up to 10 employee records, along with additional metadata for pagination.

Example Response:
{
  "count": 45,
  "next": "http://localhost:8000/api/employees/?page=3",
  "previous": "http://localhost:8000/api/employees/?page=1",
  "results": [
    {
      "id": 11,
      "name": "Charlie Brown",
      "email": "charlie.brown@example.com",
      "department": "Sales",
      "role": "Manager",
      "date_joined": "2024-10-15"
    },
    {
      "id": 12,
      "name": "Diana Prince",
      "email": "diana.prince@example.com",
      "department": "HR",
      "role": "Specialist",
      "date_joined": "2024-10-16"
    }
    // Up to 10 results per page
  ]
}

- `count`: Total number of employees.
- `next`: URL for the next page of results (or `null` if there’s no next page).
- `previous`: URL for the previous page of results (or `null` if there’s no previous page).
- `results`: An array of employee records for the current page.

### 5. Error Handling

If the specified page number exceeds the available pages, you will receive an empty `results` array with a 200 OK status:

Example Empty Page Response:
{
  "count": 45,
  "next": null,
  "previous": "http://localhost:8000/api/employees/?page=4",
  "results": []
}

If the token is invalid or missing, you will receive a 401 Unauthorized status.

Example Error Response:
{
  "detail": "Authentication credentials were not provided."
}
=======
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
>>>>>>> 2728bc94539dd1ac8438f2564751a55c7774673e
