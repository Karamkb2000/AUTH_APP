# AUTH_APP

## User Authentication and Authorization System

This project implements a User Authentication and Authorization System using the Python FastAPI framework. It includes user registration, login, role-based access control (RBAC), and JWT token-based authentication.

## Features

- **User Registration**: Allows users to create an account with username, email, and password.
- **User Login**: Authenticates users using email and password, issuing JWT tokens for subsequent requests.
- **Role-Based Access Control (RBAC)**: Implements roles (user, admin) with different permissions.
- **Protected Routes**: Certain routes are protected and accessible only to authorized users based on their roles.
- **SQLite Database**: Uses SQLite as the underlying database for ease of setup and development.
- **Interactive API Documentation**: Provides Swagger UI integration for interactive API documentation.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Karamkb2000/AUTH_APP.git
cd AUTH_APP
```

### Create and Activate a Virtual Environment (Optional but Recommended)

```bash
# Using virtualenv
virtualenv env
source env/bin/activate

# Using venv (Python 3 standard library)
python3 -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Database

To initialize the SQLite database specified in `database/database.py` using SQLAlchemy and create necessary tables based on your model definitions in `models/models.py`, run the following command:

```bash
python create_db.py
```

### Running the Application

Ensure your virtual environment is activated, then start the FastAPI application with:

```bash
python main.py
```

The application will start running at [http://localhost:8000](http://localhost:8000).

## Usage

Once the application is running, access the Swagger UI documentation to interact with the API:

- Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs).
- Test the available endpoints such as user registration, login, and protected routes.

## Endpoints

- **POST /register**: Register a new user.
- **POST /token**: Authenticate and obtain an access token.
- **GET /users/me**: Retrieve current user information.
- **GET /admin**: Access admin-only endpoint (requires admin role).

## Configuration

- **SECRET_KEY**: Replace `"your_secret_key"` in `main.py` with your preferred secret key for JWT token encryption.
- **ACCESS_TOKEN_EXPIRE_MINUTES**: Adjust token expiration time in `main.py` as needed.
