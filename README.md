# TASK_MANAGEMENT
REST API USING DJANGO FOR MANAGING TASKS


## Project Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/task-management-api.git
    cd task-management-api
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for the admin panel (optional):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the API at:**
    ```bash
    http://127.0.0.1:8000/api/
    ```


## API Endpoints

- **POST /api/register/**: Register a new user
- **POST /api/login/**: Login to get authentication tokens
- **POST /api/tasks/**: Create a new task
- **GET /api/tasks/**: List all tasks
- **GET /api/tasks/<int:pk>/**: Get a single task detail
